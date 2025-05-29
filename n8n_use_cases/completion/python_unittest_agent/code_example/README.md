# Simple Calculator

A toy Python calculator module with basic, scientific, and utility functions.

To test with the unittest agent, please move this folder to an individual repository and push to github.

## Modules

- `BaseCalculator`: Basic arithmetic operations.
- `ScientificCalculator`: Inherits from `BaseCalculator` and adds scientific functions.
- `utils`: Contains standalone utility functions.

## Example

```python
from calculator.scientific_calculator import ScientificCalculator

calc = ScientificCalculator()
print(calc.add(10, 5))          # 15
print(calc.square_root(16))     # 4.0