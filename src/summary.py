import math
import openai


def make(transcript):
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

    summary = ""
    i = 0
    for split in splits:
        print(f'call open ai for chunk #{i}...')

        prompt = f"Summarize following youtube video subtitles (part {i+1}). Return back only summary wihthout anything else. Don't include any other facts except those mentioned in the text. " + split
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        print(f'call open ai for chunk #{i}...DONE')
        i += 1

        print(response)
        text = response["choices"][0]["message"]["content"]  # type: ignore
        summary += text + "\n\n"

    if len(splits) <= 3:
        return summary

    prompt = "Here is a summary of a youtube video. Make shorter summary that fits in 1 paragraph. Return back only summary wihthout anything else. Don't include any other facts except those mentioned in the text. " + summary
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    summary_tldr = response["choices"][0]["message"]["content"]  # type: ignore

    final = 'TLDR\n' + summary_tldr + \
        '\nLonger version\n\n' + summary
    return final
