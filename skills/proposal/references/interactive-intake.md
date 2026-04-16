# Interactive Intake

Use this when the user is thinking out loud, giving fragments over multiple turns, or clearly does not yet have a structured proposal idea.

The job is to collect first, organize second, narrow third.

## Default Turn Behavior

For early-stage interactions:

- let the user give messy notes
- reflect those notes back in a cleaner structure
- mark what is explicit versus inferred
- add a short self-reflection on what may be over-inferred or still ambiguous
- ask only the next 1 to 3 questions that unblock progress
- carry the map forward and revise it each turn

Do not dump a long intake form unless the user explicitly asks for one.

## Logic Map Buckets

Sort the user's fragments into these buckets when relevant:

- `Facts or observations`
- `Hunches or interpretations`
- `Question candidates`
- `Outcome candidates`
- `Mechanism candidates`
- `Comparison or variation candidates`
- `Data leads`
- `Constraints`
- `Open gaps`
- `Parking Lot`

## Turn Output Shape

Use a compact structure like this:

```markdown
## What I Heard
- Facts or observations:
- Hunches or interpretations:
- Constraints:

## Logic Map
- Puzzle:
- Outcome:
- Mechanism:
- Comparison:
- Data:
- Contribution:

## What I Am Inferring
- ...

## Reflection
- ...

## Biggest Gaps
- ...

## Next Questions
1. ...
2. ...
3. ...
```

Not every bucket must be filled every turn. The point is to impose logic without pretending the idea is already complete.

The `Reflection` block should be short. It should expose the agent's current self-check, not a long hidden reasoning trace.

## Question Selection Rule

Ask the question that most reduces ambiguity at the current bottleneck.

Priority order:

1. outcome
2. unit of analysis
3. comparison or variation
4. data source
5. contribution
6. mechanism

If the user gives several possible directions, rank them and recommend one lead path rather than asking about all of them equally.

## Correction Rule

Invite lightweight correction:

- `This is my current reading of your idea; correct any part that I have imposed too aggressively.`

That keeps the interaction collaborative instead of making the user feel forced into the agent's structure.
