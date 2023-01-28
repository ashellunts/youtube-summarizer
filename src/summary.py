import openai


def make(transcript):
    tokens = len(transcript) / 3

    splits = []
    max_token = 4000
    if tokens > max_token:
        split_count = round(tokens / max_token)
        words = transcript.split()
        all_words_count = len(words)
        words_count_in_one_split = round(all_words_count/split_count)

        current_word = 0
        while current_word < all_words_count:
            words_in_split = words[current_word:current_word + words_count_in_one_split]
            splits.append(' '.join(words_in_split))
            current_word = current_word + words_count_in_one_split
    else:
        splits.append(transcript)

    print(f'transcript ready, splitted in {len(splits)} chunks')

    summary = ""
    i = 0
    for split in splits:
        print(f'call open ai for chunk #{i}...')

        prompt = "Make a 200 word summary of a text. It should start with a word SUMMARY. " + split

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=500
        )
        print(f'call open ai for chunk #{i}...DONE')
        i += 1

        print(response)

        text = response["choices"][0]["text"]  # type: ignore
        SUMMARY_WORD = "SUMMARY"
        index_of_summary_word = text.find(SUMMARY_WORD)

        if (index_of_summary_word == -1):
            result = text
        else:
            result = text[index_of_summary_word + len(SUMMARY_WORD):]

        if (result.find(": ") == 0):
            result = result[2:]

        summary += result + "\n\n"

    return summary
