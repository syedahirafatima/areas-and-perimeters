# Areas-and-perimeters

Code for calculating areas and perimeters of basic geometrical shapes.

Features

Circle, rectangle, square, triangle, parallelogram, trapezoid, and regular polygon

Simple Python API

Optional CLI for quick calculations

Type hints and docstrings for easy IDE help

Tests and examples
Formulas reference

Circle

Area: π r²

Perimeter: 2 π r

Rectangle

Area: w × h

Perimeter: 2(w + h)

Square

Area: s²

Perimeter: 4s
Triangle

Area: 0.5 × base × height

Perimeter: a + b + c

Optionally use Heron’s formula if only side lengths are known

Parallelogram

Area: base × height

Perimeter: 2(a + b)

Trapezoid (a and b are parallel sides, h is height)

Area: 0.5 × (a + b) × h

Perimeter: a + b + c + d

Regular polygon (n sides, side length s, apothem a)

Area: 0.5 × perimeter × apothem = 0.25 × n × s² × cot(π/n)

Perimeter: n × s
Keep tests simple and cover edge cases such as zero, negative, and nonnumeric inputs. Decide whether to raise ValueError for invalid values.

Error handling

Functions should raise ValueError for negative lengths, zero where not meaningful, or invalid n for polygons.

CLI should print clear messages and exit with a nonzero code on invalid input.

Performance

These formulas are O(1). There is no heavy computation. If you expect to batch process large CSV files, consider adding a small utility to stream inputs and write outputs.

Contributing

Fork the repo

Create a branch: git checkout -b feature/add-ellipse

Commit: git commit -m "Add ellipse area and perimeter approximations"

Push: git push origin feature/add-ellipse

Open a pull request

Please keep functions small, pure, and covered by tests.

License

Choose a license that fits your use case. MIT is a common default for educational tools.

Roadmap

Heron’s formula helper for triangle area by sides

Ellipse area and Ramanujan perimeter approximation

CSV and JSON batch utilities

Simple web demo with FastAPI
