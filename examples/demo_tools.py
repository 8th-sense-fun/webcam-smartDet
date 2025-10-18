#!/usr/bin/env python3
"""
Demo showing the difference between Black and Flake8
"""


def demonstrate_tools():
    """Show what Black and Flake8 do"""

    print("🎨 BLACK - CODE FORMATTER")
    print("=" * 40)
    print("✅ FIXES automatically:")
    print("   • Spacing around operators: x=1+2 → x = 1 + 2")
    print("   • Quote consistency: 'hello' → \"hello\"")
    print("   • Line breaks and indentation")
    print("   • Trailing commas in lists")
    print("   • Blank line spacing")
    print()
    print("🤖 Black is OPINIONATED - no configuration needed!")
    print("📝 Command: black src/")
    print()

    print("🔍 FLAKE8 - CODE LINTER")
    print("=" * 40)
    print("❌ FINDS problems (doesn't fix):")
    print("   • F401: Unused imports")
    print("   • E501: Lines too long (>79 chars)")
    print("   • W293: Blank lines with whitespace")
    print("   • E128: Bad indentation")
    print("   • And 200+ other checks!")
    print()
    print("🕵️ Flake8 is DETECTIVE - finds issues")
    print("📝 Command: flake8 src/")
    print()

    print("🔄 WORKFLOW:")
    print("1. Write code")
    print("2. Run: black src/     (fixes formatting)")
    print("3. Run: flake8 src/    (finds remaining issues)")
    print("4. Fix issues manually")
    print("5. Repeat until clean!")

    # Show a practical example
    print("\n📝 EXAMPLE:")
    print("Before Black:")
    print("def bad_function(x,y):")
    print("    result=x+y")
    print("    return result")
    print()
    print("After Black:")
    print("def bad_function(x, y):")
    print("    result = x + y")
    print("    return result")
    print()
    print("Flake8 might still complain:")
    print("❌ Function name should be snake_case")
    print("❌ Missing docstring")


if __name__ == "__main__":
    demonstrate_tools()
