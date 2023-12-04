def CalculateScore(input_frames):
    total_score = []
    frames = input_frames.split(" ")

    validation_errors = validate_input(frames)
    if validation_errors:
        return validation_errors

    for i, frame in enumerate(frames):
        frames[i] = list(frame)

    for i, frame in enumerate(frames[:10]):
        for score in frame:
            if score.isdigit():
                total_score.append(int(score))
            elif score == "x":
                total_score.append(10)
                total_score.extend(calculate_bonus(frames, i, 2))
            elif score == "/":
                total_score.append(10 - total_score[-1])
                total_score.extend(calculate_bonus(frames, i, 1))

    return sum(total_score)


def calculate_bonus(frames, current_frame_index, bonus_rolls):
    bonus_scores = []
    rolls_counted = 0

    for next_frame in frames[current_frame_index + 1 :]:
        for roll in next_frame:
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
    errors = []
    if not (10 <= len(input_frames) <= 12):
        errors.append(
            "Invalid number of frames. There should be between 10 and 12 frames."
        )

    return errors
