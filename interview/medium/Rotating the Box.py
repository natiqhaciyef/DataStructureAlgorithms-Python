def rotateTheBox(boxGrid):
    m = len(boxGrid)
    n = len(boxGrid[0])

    # Step 1: Apply gravity (stones fall to the right)
    for i in range(m):
        # Start the empty pointer at the rightmost edge
        empty_index = n - 1
        # Scan from right to left
        for j in range(n - 1, -1, -1):
            if boxGrid[i][j] == '*':
                # Obstacle resets the empty pointer
                empty_index = j - 1
            elif boxGrid[i][j] == '#':
                # Move the stone to the lowest empty spot
                # Only move if the empty spot isn't the current spot
                if empty_index != j:
                    boxGrid[i][empty_index] = '#'
                    boxGrid[i][j] = '.'
                # Decrement empty spot since it's now filled
                empty_index -= 1

    # Step 2: Rotate 90 degrees clockwise
    # New matrix will be n x m
    rotated = [['.' for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            # Formula for 90-degree clockwise rotation
            rotated[j][m - 1 - i] = boxGrid[i][j]

    return rotated