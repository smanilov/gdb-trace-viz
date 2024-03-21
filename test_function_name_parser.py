import unittest
from parse_backtrace import parse_function_name


def assertParsedFunctionName(testcase, function_part, expected_function_name):
    function_name = parse_function_name(function_part)
    testcase.assertEqual(function_name, expected_function_name)


class TestParseFunctionName_ManualTests(unittest.TestCase):
    def test_simple_function_name(self):
        assertParsedFunctionName(self, "foo()", "foo")

    def test_operator_function_name(self):
        assertParsedFunctionName(self, "operator()()", "operator()")

    def test_function_with_template_arguments(self):
        assertParsedFunctionName(
            self,
            "llvm::function_ref<void ()>::operator()() const",
            "llvm::function_ref<void ()>::operator()",
        )


class TestParseFunctionName_GeneratedTests(unittest.TestCase):
    def test_1(self):
        assertParsedFunctionName(
            self,
            "clang::Lexer::Lex (this=0x555563f55590, Result=...)",
            "clang::Lexer::Lex",
        )

    def test_2(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::CLK_Lexer (P=..., Result=...)",
            "clang::Preprocessor::CLK_Lexer",
        )

    def test_3(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)",
            "clang::Preprocessor::Lex",
        )

    def test_4(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ConsumeToken (this=0x55556401fe00)",
            "clang::Parser::ConsumeToken",
        )

    def test_5(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::Initialize (this=0x55556401fe00)",
            "clang::Parser::Initialize",
        )

    def test_6(self):
        assertParsedFunctionName(
            self,
            "clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)",
            "clang::ParseAST",
        )

    def test_7(self):
        assertParsedFunctionName(
            self,
            "clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::ASTFrontendAction::ExecuteAction",
        )

    def test_8(self):
        assertParsedFunctionName(
            self,
            "clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::CodeGenAction::ExecuteAction",
        )

    def test_9(self):
        assertParsedFunctionName(
            self,
            "clang::FrontendAction::Execute (this=0x555563f9d9c0)",
            "clang::FrontendAction::Execute",
        )

    def test_10(self):
        assertParsedFunctionName(
            self,
            "clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)",
            "clang::CompilerInstance::ExecuteAction",
        )

    def test_11(self):
        assertParsedFunctionName(
            self,
            "clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)",
            "clang::ExecuteCompilerInvocation",
        )

    def test_12(self):
        assertParsedFunctionName(self, "cc1_main (Argv=...,", "cc1_main")

    def test_13(self):
        assertParsedFunctionName(
            self, "ExecuteCC1Tool (ArgV=..., ToolContext=...)", "ExecuteCC1Tool"
        )

    def test_14(self):
        assertParsedFunctionName(
            self,
            "clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)",
            "clang_main",
        )

    def test_15(self):
        assertParsedFunctionName(self, "main (argc=65, argv=0x7fffffffd738)", "main")

    def test_16(self):
        assertParsedFunctionName(
            self,
            "clang::Lexer::Lex (this=0x5555640173c0, Result=...)",
            "clang::Lexer::Lex",
        )

    def test_17(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::CLK_Lexer (P=..., Result=...)",
            "clang::Preprocessor::CLK_Lexer",
        )

    def test_18(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)",
            "clang::Preprocessor::Lex",
        )

    def test_19(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ConsumeToken (this=0x55556401fe00)",
            "clang::Parser::ConsumeToken",
        )

    def test_20(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ConsumeAnyToken (this=0x55556401fe00,",
            "clang::Parser::ConsumeAnyToken",
        )

    def test_21(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarationSpecifiers (this=0x55556401fe00, DS=...,",
            "clang::Parser::ParseDeclarationSpecifiers",
        )

    def test_22(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarationSpecifiers (this=0x55556401fe00, DS=...,",
            "clang::Parser::ParseDeclarationSpecifiers",
        )

    def test_23(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclOrFunctionDefInternal (this=0x55556401fe00,",
            "clang::Parser::ParseDeclOrFunctionDefInternal",
        )

    def test_24(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarationOrFunctionDefinition (this=0x55556401fe00,",
            "clang::Parser::ParseDeclarationOrFunctionDefinition",
        )

    def test_25(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseExternalDeclaration (this=0x55556401fe00, Attrs=...,",
            "clang::Parser::ParseExternalDeclaration",
        )

    def test_26(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseTopLevelDecl (this=0x55556401fe00, Result=...,",
            "clang::Parser::ParseTopLevelDecl",
        )

    def test_27(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseFirstTopLevelDecl (this=0x55556401fe00, Result=...,",
            "clang::Parser::ParseFirstTopLevelDecl",
        )

    def test_28(self):
        assertParsedFunctionName(
            self,
            "clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)",
            "clang::ParseAST",
        )

    def test_29(self):
        assertParsedFunctionName(
            self,
            "clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::ASTFrontendAction::ExecuteAction",
        )

    def test_30(self):
        assertParsedFunctionName(
            self,
            "clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::CodeGenAction::ExecuteAction",
        )

    def test_31(self):
        assertParsedFunctionName(
            self,
            "clang::FrontendAction::Execute (this=0x555563f9d9c0)",
            "clang::FrontendAction::Execute",
        )

    def test_32(self):
        assertParsedFunctionName(
            self,
            "clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)",
            "clang::CompilerInstance::ExecuteAction",
        )

    def test_33(self):
        assertParsedFunctionName(
            self,
            "clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)",
            "clang::ExecuteCompilerInvocation",
        )

    def test_34(self):
        assertParsedFunctionName(self, "cc1_main (Argv=...,", "cc1_main")

    def test_35(self):
        assertParsedFunctionName(
            self, "ExecuteCC1Tool (ArgV=..., ToolContext=...)", "ExecuteCC1Tool"
        )

    def test_36(self):
        assertParsedFunctionName(
            self,
            "clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)",
            "clang_main",
        )

    def test_37(self):
        assertParsedFunctionName(self, "main (argc=65, argv=0x7fffffffd738)", "main")

    def test_38(self):
        assertParsedFunctionName(
            self,
            "clang::Lexer::Lex (this=0x5555640173c0, Result=...)",
            "clang::Lexer::Lex",
        )

    def test_39(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::CLK_Lexer (P=..., Result=...)",
            "clang::Preprocessor::CLK_Lexer",
        )

    def test_40(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)",
            "clang::Preprocessor::Lex",
        )

    def test_41(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::PeekAhead (this=0x555563fa1190, N=1)",
            "clang::Preprocessor::PeekAhead",
        )

    def test_42(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::LookAhead (this=0x555563fa1190, N=0)",
            "clang::Preprocessor::LookAhead",
        )

    def test_43(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::NextToken (this=0x55556401fe00)",
            "clang::Parser::NextToken",
        )

    def test_44(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclaratorInternal (this=0x55556401fe00, D=...,",
            "clang::Parser::ParseDeclaratorInternal",
        )

    def test_45(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarator(clang::Declarator&)::$_0::operator()() const (",
            "clang::Parser::ParseDeclarator",
        )

    def test_46(self):
        assertParsedFunctionName(
            self,
            "llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>(long) (callable=140737488326568)",
            "llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>",
        )

    def test_47(self):
        assertParsedFunctionName(
            self,
            "llvm::function_ref<void ()>::operator()() const (this=0x7fffffff8f00)",
            "llvm::function_ref<void ()>::operator()",
        )

    def test_48(self):
        assertParsedFunctionName(
            self,
            "clang::runWithSufficientStackSpace(llvm::function_ref<void ()>, llvm::function_ref<void ()>) (Diag=..., Fn=...)",
            "clang::runWithSufficientStackSpace",
        )

    def test_49(self):
        assertParsedFunctionName(
            self,
            "clang::Sema::runWithSufficientStackSpace(clang::SourceLocation, llvm::function_ref<void ()>) (this=0x555564012cd0, Loc=..., Fn=...)",
            "clang::Sema::runWithSufficientStackSpace",
        )

    def test_50(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarator (this=0x55556401fe00, D=...)",
            "clang::Parser::ParseDeclarator",
        )

    def test_51(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclGroup (this=0x55556401fe00, DS=...,",
            "clang::Parser::ParseDeclGroup",
        )

    def test_52(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclOrFunctionDefInternal (this=0x55556401fe00,",
            "clang::Parser::ParseDeclOrFunctionDefInternal",
        )

    def test_53(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarationOrFunctionDefinition (this=0x55556401fe00,",
            "clang::Parser::ParseDeclarationOrFunctionDefinition",
        )

    def test_54(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseExternalDeclaration (this=0x55556401fe00, Attrs=...,",
            "clang::Parser::ParseExternalDeclaration",
        )

    def test_55(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseTopLevelDecl (this=0x55556401fe00, Result=...,",
            "clang::Parser::ParseTopLevelDecl",
        )

    def test_56(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseFirstTopLevelDecl (this=0x55556401fe00, Result=...,",
            "clang::Parser::ParseFirstTopLevelDecl",
        )

    def test_57(self):
        assertParsedFunctionName(
            self,
            "clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)",
            "clang::ParseAST",
        )

    def test_58(self):
        assertParsedFunctionName(
            self,
            "clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::ASTFrontendAction::ExecuteAction",
        )

    def test_59(self):
        assertParsedFunctionName(
            self,
            "clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::CodeGenAction::ExecuteAction",
        )

    def test_60(self):
        assertParsedFunctionName(
            self,
            "clang::FrontendAction::Execute (this=0x555563f9d9c0)",
            "clang::FrontendAction::Execute",
        )

    def test_61(self):
        assertParsedFunctionName(
            self,
            "clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)",
            "clang::CompilerInstance::ExecuteAction",
        )

    def test_62(self):
        assertParsedFunctionName(
            self,
            "clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)",
            "clang::ExecuteCompilerInvocation",
        )

    def test_63(self):
        assertParsedFunctionName(self, "cc1_main (Argv=...,", "cc1_main")

    def test_64(self):
        assertParsedFunctionName(
            self, "ExecuteCC1Tool (ArgV=..., ToolContext=...)", "ExecuteCC1Tool"
        )

    def test_65(self):
        assertParsedFunctionName(
            self,
            "clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)",
            "clang_main",
        )

    def test_66(self):
        assertParsedFunctionName(self, "main (argc=65, argv=0x7fffffffd738)", "main")

    def test_67(self):
        assertParsedFunctionName(
            self,
            "clang::Lexer::Lex (this=0x5555640173c0, Result=...)",
            "clang::Lexer::Lex",
        )

    def test_68(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::CLK_Lexer (P=..., Result=...)",
            "clang::Preprocessor::CLK_Lexer",
        )

    def test_69(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)",
            "clang::Preprocessor::Lex",
        )

    def test_70(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::CachingLex (this=0x555563fa1190, Result=...)",
            "clang::Preprocessor::CachingLex",
        )

    def test_71(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::CLK_CachingLexer (P=..., Result=...)",
            "clang::Preprocessor::CLK_CachingLexer",
        )

    def test_72(self):
        assertParsedFunctionName(
            self,
            "clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)",
            "clang::Preprocessor::Lex",
        )

    def test_73(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ConsumeParen (this=0x55556401fe00)",
            "clang::Parser::ConsumeParen",
        )

    def test_74(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::isCXXFunctionDeclarator (this=0x55556401fe00,",
            "clang::Parser::isCXXFunctionDeclarator",
        )

    def test_75(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDirectDeclarator (this=0x55556401fe00, D=...)",
            "clang::Parser::ParseDirectDeclarator",
        )

    def test_76(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclaratorInternal (this=0x55556401fe00, D=...,",
            "clang::Parser::ParseDeclaratorInternal",
        )

    def test_77(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarator(clang::Declarator&)::$_0::operator()() const (",
            "clang::Parser::ParseDeclarator",
        )

    def test_78(self):
        assertParsedFunctionName(
            self,
            "llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>(long) (callable=140737488326568)",
            "llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>",
        )

    def test_79(self):
        assertParsedFunctionName(
            self,
            "llvm::function_ref<void ()>::operator()() const (this=0x7fffffff8f00)",
            "llvm::function_ref<void ()>::operator()",
        )

    def test_80(self):
        assertParsedFunctionName(
            self,
            "clang::runWithSufficientStackSpace(llvm::function_ref<void ()>, llvm::function_ref<void ()>) (Diag=..., Fn=...)",
            "clang::runWithSufficientStackSpace",
        )

    def test_81(self):
        assertParsedFunctionName(
            self,
            "clang::Sema::runWithSufficientStackSpace(clang::SourceLocation, llvm::function_ref<void ()>) (this=0x555564012cd0, Loc=..., Fn=...)",
            "clang::Sema::runWithSufficientStackSpace",
        )

    def test_82(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarator (this=0x55556401fe00, D=...)",
            "clang::Parser::ParseDeclarator",
        )

    def test_83(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclGroup (this=0x55556401fe00, DS=...,",
            "clang::Parser::ParseDeclGroup",
        )

    def test_84(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclOrFunctionDefInternal (this=0x55556401fe00,",
            "clang::Parser::ParseDeclOrFunctionDefInternal",
        )

    def test_85(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseDeclarationOrFunctionDefinition (this=0x55556401fe00,",
            "clang::Parser::ParseDeclarationOrFunctionDefinition",
        )

    def test_86(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseExternalDeclaration (this=0x55556401fe00, Attrs=...,",
            "clang::Parser::ParseExternalDeclaration",
        )

    def test_87(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseTopLevelDecl (this=0x55556401fe00, Result=...,",
            "clang::Parser::ParseTopLevelDecl",
        )

    def test_88(self):
        assertParsedFunctionName(
            self,
            "clang::Parser::ParseFirstTopLevelDecl (this=0x55556401fe00, Result=...,",
            "clang::Parser::ParseFirstTopLevelDecl",
        )

    def test_89(self):
        assertParsedFunctionName(
            self,
            "clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)",
            "clang::ParseAST",
        )

    def test_90(self):
        assertParsedFunctionName(
            self,
            "clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::ASTFrontendAction::ExecuteAction",
        )

    def test_91(self):
        assertParsedFunctionName(
            self,
            "clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)",
            "clang::CodeGenAction::ExecuteAction",
        )

    def test_92(self):
        assertParsedFunctionName(
            self,
            "clang::FrontendAction::Execute (this=0x555563f9d9c0)",
            "clang::FrontendAction::Execute",
        )

    def test_93(self):
        assertParsedFunctionName(
            self,
            "clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)",
            "clang::CompilerInstance::ExecuteAction",
        )

    def test_94(self):
        assertParsedFunctionName(
            self,
            "clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)",
            "clang::ExecuteCompilerInvocation",
        )

    def test_95(self):
        assertParsedFunctionName(self, "cc1_main (Argv=...,", "cc1_main")

    def test_96(self):
        assertParsedFunctionName(
            self, "ExecuteCC1Tool (ArgV=..., ToolContext=...)", "ExecuteCC1Tool"
        )

    def test_97(self):
        assertParsedFunctionName(
            self,
            "clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)",
            "clang_main",
        )

    def test_98(self):
        assertParsedFunctionName(self, "main (argc=65, argv=0x7fffffffd738)", "main")


if __name__ == "__main__":
    unittest.main()
