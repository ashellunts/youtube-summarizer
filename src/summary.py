import asyncio
import math
import openai_async
import os
import time


async def open_ai_call(i, prompt):
    import time
    start_time = time.time()
    print(f'ASYNC2 call open ai for chunk #{i}..., start time {start_time}')
    response = await openai_async.chat_complete(
        os.environ["OPENAI_API_KEY"],
        timeout=20,
        payload={
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        }
    )
    duration_in_second_and_milliseconds = (time.time() - start_time)
    print(f'call open ai for chunk #{i}...DONE, took {duration_in_second_and_milliseconds} seconds')
    return response.json()["choices"][0]["message"]["content"]  # type: ignore


async def make(transcript):
    tokens = len(transcript) / 4
    print("len = ", len(transcript))
    print("tokens = ", tokens)
    splits = []
    max_token = 4000
    if tokens > max_token:
        split_count = int(math.ceil(tokens / max_token))
        words = transcript.split()
        all_words_count = len(words)
        words_count_in_one_split = int(math.ceil(all_words_count/split_count))
        print(f"all words {all_words_count}")
        print(f"words count in 1 split {words_count_in_one_split}")
        current_word = 0
        while current_word < all_words_count:
            print(f"split from {current_word} to {current_word+words_count_in_one_split}")
            words_in_split = words[current_word:current_word + words_count_in_one_split]
            new_split = ' '.join(words_in_split)
            splits.append(new_split)
            current_word = current_word + words_count_in_one_split
    else:
        splits.append(transcript)

    print(f'transcript ready, splitted in {len(splits)} chunks')

    tasks = []
    for i, split in enumerate(splits):
        prompt = f"Summarize following youtube video subtitles (part {i+1}). Return back only summary wihthout anything else. Don't include any other facts except those mentioned in the text. " + split
        tasks.append(open_ai_call(i, prompt))
    start_time = time.time()
    responses = await asyncio.gather(*tasks)
    duration_in_second_and_milliseconds = (time.time() - start_time)
    print(f'ALL requests in parallel took {duration_in_second_and_milliseconds} seconds')

    summary = []
    summary_for_big_summary = ""
    i = 0
    for text in responses:
        i += 1
        summary.append(text)
        summary_for_big_summary += text + "\n\n"

    if len(splits) <= 3:
        return summary

    prompt = "Here is a summary of a youtube video. Make shorter summary that fits in 1 paragraph. Return back only summary wihthout anything else. Don't include any other facts except those mentioned in the text. " + summary_for_big_summary

    summary_tldr = await open_ai_call(0, prompt)

    result = {
        "tldr": summary_tldr,
        "longer_summary": summary
    }
    return result
