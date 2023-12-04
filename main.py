class BowlinCalculator:
    def __init__(self):
        self.total_score = None
        self.frames = None
        self.current_frame_index = None

    def calculate_score(self, input_frames):
        self.total_score = []
        self.frames = input_frames.split(" ")

        self.validate_input()
        for i, frame in enumerate(self.frames):
            self.frames[i] = list(frame)

        for self.current_frame_index, frame in enumerate(self.frames[:10]):
            for score in frame:
                if score.isdigit():
                    self.total_score.append(int(score))
                elif score == "x":
                    self.total_score.append(10)
                    self.total_score.extend(self.calculate_bonus(score))
                elif score == "/":
                    self.total_score.append(10 - self.total_score[-1])
                    self.total_score.extend(self.calculate_bonus(score))

        return sum(self.total_score)

    def calculate_bonus(self, bonus_type):
        bonus_scores = []
        rolls_counted = 0

        for next_frame in self.frames[self.current_frame_index + 1 :]:
            for roll in next_frame:
                self.validate_bonus(bonus_type)

                bonus_rolls = 1 if bonus_type == "/" else 2
                if rolls_counted == bonus_rolls:
                    return bonus_scores

                if roll == "x":
                    bonus_scores.append(10)
                elif roll.isdigit():
                    bonus_scores.append(int(roll))
                elif roll == "/":
                    bonus_scores.append(10 - bonus_scores[-1])

                rolls_counted += 1

        return bonus_scores

    def validate_input(self):
        if not (10 <= len(self.frames) <= 12):
            raise Exception(
                "Invalid number of frames. There should be between 10 and 12 frames."
            )

        for frame in self.frames:
            try:
                if sum([int(x) for x in frame]) > 10:
                    raise Exception("One frame cannot be higher than 10.")
            except ValueError:
                pass

    def validate_bonus(self, bonus_type):
        if bonus_type == "x" and self.frames[self.current_frame_index + 1][0] == "/":
            raise Exception("/ cannot follow x")
