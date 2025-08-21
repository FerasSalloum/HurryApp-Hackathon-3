// const frames = [2, 3, 6, 4, 5, 8, 7, 1];
// const frames = [1, 2, 3, 5, 6];
// const frames = [16, 1, 5, 2, 10, 3, 11, 6,];
// const frames = [1, 2, 3, 5, 6, 16, 20, 30, 55];

// const frames = [1, 2, 3, 5, 6, 10, 11, 16];
const findMissingRanges = (frames) => {
    let result = {
        gaps: [],
        longest_gap: [],
        missing_count: 0
    };
    // #region ترتيب المصفوفة
    for (let i = 0; i < frames.length; i++) {
        let minIndex = i;
        for (let j = i + 1; j < frames.length; j++) {
            if (frames[j] < frames[minIndex]) {
                minIndex = j;
            }
        }
        [frames[i], frames[minIndex]] = [frames[minIndex], frames[i]];
    }
    // #endregion 
    // #region ايجاد الفجوات
    // وضع اول فجوة
    if (frames[0] != 1) {
        frames.unshift(0)
    }
    for (let i = 0; i < frames.length - 1; i++) {
        let start = frames[i];
        let end = frames[i + 1];
        if (end > start + 1) {
            let gapStart = start + 1;
            let gapEnd = end - 1;
            result.gaps.push([gapStart, gapEnd]);
            result.missing_count += gapEnd - gapStart + 1;
            // #region تحديد أطول فجوة
            if (
                result.longest_gap.length === 0 ||
                gapEnd - gapStart > result.longest_gap[1] - result.longest_gap[0]
            ) {
                result.longest_gap = [gapStart, gapEnd];
            }
            // #endregion
        }
    }
    // #endregion

    return result;
};
// console.log(findMissingRanges(frames));
