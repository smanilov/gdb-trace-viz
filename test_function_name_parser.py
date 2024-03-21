import unittest
from parse_backtrace import parse_function_name

class TestParseFunctionName(unittest.TestCase):
    def test_simple_function_name(self):
        function_part = "foo()"
        function_name = parse_function_name(function_part)
        self.assertEqual(function_name, "foo")

    def test_operator_function_name(self):
        function_part = "operator()()"
        function_name = parse_function_name(function_part)
        self.assertEqual(function_name, "operator()")

    def test_function_with_template_arguments(self):
        function_part = "llvm::function_ref<void ()>::operator()() const"
        function_name = parse_function_name(function_part)
        self.assertEqual(function_name, "llvm::function_ref<void ()>::operator()")

if __name__ == "__main__":
    unittest.main()

