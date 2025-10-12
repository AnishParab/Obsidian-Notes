# `iostream`
- Deals with basic input/output.

### `std::cout`
- Send data to the console to be printed as text.
- `<<` ---> **insertion operator**.

### `std::cin`
- Character input.
- `>>` ---> extraction operator.

### `std::endl`
- To output a new line on the console.

---
# `std::cout` is buffered
- Statements in our program request output to be sent to the console.
- Output is stored in a **buffer**.
- Periodically, the buffer is **flushed**.
- All the output is transferred to the destination.
- It follows FIFO ordering.

---
# Why `std::endl` in inefficient
- Using `std::endl` is often inefficient, as it actually does two jobs.
- It outputs a newline (moving the cursor to the next line of the console), and it flushes the buffer (which is slow).
- If we output multiple lines of text ending with `std::endl`, we will get multiple flushes, which is slow and probably unnecessary.

---
# Hence use `\n` instead of `std::endl`
- Special character.
- Moves the cursor to the next line of the console, without causing _flush_.
``` cpp
#include <iostream> // for std::cout

int main()
{
    int x{ 5 };
    std::cout << "x is equal to: " << x << '\n'; // single quoted (by itself) (conventional)
    std::cout << "Yep." << "\n";                 // double quoted (by itself) (unconventional but okay)
    std::cout << "And that's all, folks!\n";     // between double quotes in existing text (conventional)
    return 0;
}
```
- Even though ‘\n’ is represented in source code as two symbols, it is treated by the compiler as a single linefeed (LF) character (with ASCII value 10), and thus is conventionally single quoted

---
# `std::cin` is buffered
- The individual characters you enter as input are added to the end of an input buffer (inside `std::cin`). The enter key (pressed to submit the data) is also stored as a `'\n'` character.
- The extraction operator ‘>>’ removes characters from the front of the input buffer and converts them into a value that is assigned (via copy-assignment) to the associated variable. This variable can then be used in subsequent statements.

### Example:
``` cpp
#include <iostream>  // for std::cout and std::cin

int main()
{
    std::cout << "Enter two numbers: ";

    int x{};
    std::cin >> x;

    int y{};
    std::cin >> y;

    std::cout << "You entered " << x << " and " << y << '\n';

    return 0;
}
```
This program inputs to two variables (this time as separate statements). We’ll run this program twice.

**Run #1:**
- When `std::cin >> x;` is encountered, the program will wait for input. Enter the value `4`. The input `4\n` goes into the input buffer, and the value `4` is extracted to variable `x`.
- When `std::cin >> y;` is encountered, the program will again wait for input. Enter the value `5`. The input `5\n` goes into the input buffer, and the value `5` is extracted to variable `y`. Finally, the program will print `You entered 4 and 5`.

**Run #2:**
- When `std::cin >> x` is encountered, the program will wait for input. Enter `4 5`. The input `4 5\n` goes into the input buffer, but only the `4` is extracted to variable `x` (extraction stops at the space).
- When `std::cin >> y` is encountered, the program will _not_ wait for input. Instead, the `5` that is still in the input buffer is extracted to variable `y`. The program then prints `You entered 4 and 5`.
- Note that in run 2, the program didn’t wait for the user to enter additional input when extracting to variable `y` because there was already prior input in the input buffer that could be used.

---
