def CalculateScore(input_frames):
    total_score = []
    frames = input_frames.split(" ")

    validate_input(frames)
    for i, frame in enumerate(frames):
        frames[i] = list(frame)

    for i, frame in enumerate(frames[:10]):
        for score in frame:
            if score.isdigit():
                total_score.append(int(score))
            elif score == "x":
                total_score.append(10)
                total_score.extend(calculate_bonus(frames, i, score))
            elif score == "/":
                total_score.append(10 - total_score[-1])
                total_score.extend(calculate_bonus(frames, i, score))

    return sum(total_score)


def calculate_bonus(frames, current_frame_index, bonus_type):
    bonus_scores = []
    rolls_counted = 0

    for next_frame in frames[current_frame_index + 1 :]:
        for roll in next_frame:
            validate_bonus(frames, current_frame_index, bonus_type)

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


def validate_input(input_frames):
    if not (10 <= len(input_frames) <= 12):
        raise Exception(
            "Invalid number of frames. There should be between 10 and 12 frames."
        )

    for frame in input_frames:
        try:
            if sum([int(x) for x in frame]) > 10:
                raise Exception("One frame cannot be higher than 10.")
        except ValueError:
            pass


def validate_bonus(frames, current_frame_index, bonus_type):
    if bonus_type == "x" and frames[current_frame_index + 1][0] == "/":
        raise Exception("/ cannot follow x")
