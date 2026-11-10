"""Compare untrained and trained agents on the same task."""

from agent import train, evaluate, demonstrate


if __name__ == "__main__":
    print("UNTRAINED AGENT")
    print("All action values start at zero.")
    evaluate({})

    print("\nTRAINING")
    learned_values = train(seed=42)

    print("\nTRAINED AGENT")
    evaluate(learned_values)
    demonstrate(learned_values)