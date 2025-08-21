def find_missing_ranges(frames: list[int]) -> dict:
    result = {
        "gaps": [],
        "longest_gap": [],
        "missing_count": 0
    }

    for i in range(len(frames)):
        min_index = i
        for j in range(i + 1, len(frames)):
            if frames[j] < frames[min_index]:
                min_index = j
        frames[i], frames[min_index] = frames[min_index], frames[i]

    for i in range(len(frames) - 1):
        start = frames[i]
        end = frames[i + 1]
        if end > start + 1:
            gap_start = start + 1
            gap_end = end - 1
            result["gaps"].append([gap_start, gap_end])
            result["missing_count"] += gap_end - gap_start + 1
            if (
                len(result["longest_gap"]) == 0
                or (gap_end - gap_start) > (result["longest_gap"][1] - result["longest_gap"][0])
            ):
                result["longest_gap"] = [gap_start, gap_end]

    return result


# مثال للتشغيل
frames = [1, 2, 3, 5, 6, 10, 11, 16]
print(find_missing_ranges(frames))
