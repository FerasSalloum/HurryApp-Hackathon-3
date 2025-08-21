# frames = [2, 3, 6, 4, 5, 8, 7, 1]
# frames = [1, 2, 3, 5, 6]
# frames = [16, 1, 5, 2, 10, 3, 11, 6]
# frames = [1, 2, 3, 5, 6, 16, 20, 30, 55]

# frames = [1, 2, 3, 5, 6, 10, 11, 16]
def find_missing_ranges(frames):
    result = {
        "gaps": [],
        "longest_gap": [],
        "missing_count": 0
    }

    #   ترتيب المصفوفة  
    for i in range(len(frames)):
        minIndex = i
        for j in range(i + 1, len(frames)):
            if frames[j] < frames[minIndex]:
                minIndex = j
        frames[i], frames[minIndex] = frames[minIndex], frames[i]

    #   إيجاد الفجوات  
    # وضع أول فجوة
    if frames[0] > 1:
        # frames.insert(0, 0)
        result["gaps"].append([1, frames[0] - 1])
        result["missing_count"] += frames[0] - 1

    for i in range(len(frames) - 1):
        start = frames[i]
        end = frames[i + 1]
        if end > start + 1:
            gapStart = start + 1
            gapEnd = end - 1
            result["gaps"].append([gapStart, gapEnd])
            result["missing_count"] += gapEnd - gapStart + 1
            #   تحديد أطول فجوة  
            if (len(result["longest_gap"]) == 0 or
                gapEnd - gapStart > result["longest_gap"][0][1] - result["longest_gap"][0][0]):
                result["longest_gap"] = [[gapStart, gapEnd]]
            # اضافة الفجوات متساوية الطول
            elif gapEnd - gapStart == result["longest_gap"][0][1] - result["longest_gap"][0][0]:
                result["longest_gap"].append([gapStart, gapEnd])

    return result