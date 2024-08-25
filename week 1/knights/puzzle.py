from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


knowledgeBase = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
)
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    knowledgeBase,
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    knowledgeBase,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    knowledgeBase,
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    knowledgeBase,
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    # most difficult
    Or(
        Implication(
            BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
        ),
        Implication(
            BKnave,
            (Not(Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))),
        ),
    ),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
)

# Chat gpt practice examples


# Puzzle 4
# A says: "B is a knave."
# B says nothing.

knowledge4 = And(
    knowledgeBase,
    Implication (AKnight, BKnave),
    Implication (AKnave, Not(BKnave))
)

# Puzzle 5
# A says: "B is a knight."
# B says: "C is a knave."
# C says: "A is a knight."

knowledge5 = And(
    knowledgeBase,
    Implication (AKnight, BKnight),
    Implication (AKnave, Not(BKnight)),
    Implication (BKnight, CKnave),
    Implication (BKnave, Not(CKnave)),
    Implication (CKnight, AKnight),
    Implication (CKnave, Not(AKnight))
)

# Puzzle 6
# A says: "B is a knight if and only if C is a knave."
# B says: "A is either a knight or C is a knight, but not both."
# C says: "B is a knight."

knowledge6 = And(
    knowledgeBase,
    Implication (AKnight, Implication (BKnight,CKnave)),
    Implication (AKnave, Not(Implication (BKnight,CKnave))),
    Implication (BKnight, Or(AKnight,CKnight)),
    Implication (BKnave, Not(Or(AKnight,CKnight))),
    Implication (CKnight,BKnight),
    Implication (CKnave, Not(BKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
        ("Puzzle 4", knowledge4),
        ("Puzzle 5", knowledge5),
        ("Puzzle 6", knowledge6),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
