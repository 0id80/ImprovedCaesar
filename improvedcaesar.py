from json import load


class ImprovedCaesar:
    def __init__(self):
        with open("languages.json", "r", encoding="utf-8") as file:
            self.languages = load(file)

    @staticmethod
    def change_index(char, language, step, step_offset, state) -> int:
        offset_index = language[state].index(char) + step + step_offset
        while offset_index > (language["len"] - 1):
            offset_index = offset_index - language["len"]
        return offset_index

    def encoder(self, text, step=0) -> str:
        text = list(text)
        step_offset = 0
        for char, i_char in zip(text, range(0, len(text)+1)):
            if char != " ":
                for language in self.languages:
                    if char in self.languages[language]["full"]:
                        if char in self.languages[language]["upper"]:
                            text[i_char] = self.languages[language]["upper"][self.change_index(char=char,
                                                                                               language=self.languages[language],
                                                                                               step=step,
                                                                                               step_offset=step_offset,
                                                                                               state="upper")]
                        else:
                            text[i_char] = self.languages[language]["lower"][self.change_index(char=char,
                                                                                               language=self.languages[language],
                                                                                               step=step,
                                                                                               step_offset=step_offset,
                                                                                               state="lower")]
            step_offset += step
        return "".join(text)

    def decoder(self, text, step=0) -> str:

        return text
