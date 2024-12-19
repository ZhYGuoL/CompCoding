sum((
    all(
        n in range(
            eval(l)[2],
            eval(l)[3] + 1
        )
        for n in range(
            eval(l)[0],
            eval(l)[1] + 1
        )
    ) or all(
        n in range(
            eval(l)[0],
            eval(l)[1] + 1
        )
        for n in range(
            eval(l)[2],
            eval(l)[3] + 1
        )
    )
)
ProblemInput = [for l in open("Day4Input.txt").read().split('-')]



# sum((
    # any(
        # n in range(
            # eval(l)[2],
            # eval(l)[3] + 1
        # )
        # for n in range(
            # eval(l)[0],
            # eval(l)[1] + 1
        # )
    # ) or any(
        # n in range(
            # eval(l)[0],
            # eval(l)[1] + 1
        # )
        # for n in range(
            # eval(l)[2],
            # eval(l)[3] + 1
        # )
    # )
# )
# for l in open("Day4Input.txt").read().replace(
    # "-",
    # ","
# ).split())