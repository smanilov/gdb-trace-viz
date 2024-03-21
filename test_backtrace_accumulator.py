import unittest
from backtrace_accumulator import BacktraceAccumulator


class TestBacktraceAccumulator(unittest.TestCase):
    def test_process_example(self):
        accumulator = BacktraceAccumulator()

        backtrace = "#1 FunctionA\n#2 FunctionB\n#3 FunctionC\n"

        expected_dot_code = (
            "digraph Backtrace {\n"
            "    node [shape=box]\n"
            '    "FunctionC" -> "FunctionB"\n'
            '    "FunctionB" -> "FunctionA"\n'
            "}"
        )

        result_dot_code = accumulator.process(backtrace)

        self.assertEqual(result_dot_code, expected_dot_code)

    def test_process_real(self):
        accumulator = BacktraceAccumulator()

        backtrace = """#0  clang::Lexer::Lex (this=0x555563f55590, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Lexer.cpp:3623
#1  0x0000555560eb673c in clang::Preprocessor::CLK_Lexer (P=..., Result=...)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Lex/Preprocessor.h:2903
#2  0x000055556349ddc8 in clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Preprocessor.cpp:869
#3  0x0000555560eb0d2e in clang::Parser::ConsumeToken (this=0x55556401fe00)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Parse/Parser.h:497
#4  0x0000555560ea79f3 in clang::Parser::Initialize (this=0x55556401fe00)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:576
#5  0x0000555560ea3118 in clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseAST.cpp:156
#6  0x000055555daab15b in clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1183
#7  0x000055555d57eda6 in clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/CodeGen/CodeGenAction.cpp:1153
#8  0x000055555daaab7c in clang::FrontendAction::Execute (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1069
#9  0x000055555d9cc61c in clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/CompilerInstance.cpp:1057
#10 0x000055555dc788f1 in clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)
    at /media/new/open_source/llvm-project/source/clang/lib/FrontendTool/ExecuteCompilerInvocation.cpp:272
#11 0x000055555a92fb9f in cc1_main (Argv=...,
    Argv0=0x7fffffffdca6 "/media/new/open_source/llvm-project/build-debug/bin/clang-18",
    MainAddr=0x55555a91ebb0 <GetExecutablePath[abi:cxx11](char const*, bool)>)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/cc1_main.cpp:294
#12 0x000055555a920372 in ExecuteCC1Tool (ArgV=..., ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:366
#13 0x000055555a91f0b4 in clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:407
#14 0x000055555a95372d in main (argc=65, argv=0x7fffffffd738)
    at /media/new/open_source/llvm-project/build-debug/tools/clang/tools/driver/clang-driver.cpp:15
"""
        accumulator.process(backtrace)

        backtrace = """#0  clang::Lexer::Lex (this=0x5555640173c0, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Lexer.cpp:3623
#1  0x0000555560eb673c in clang::Preprocessor::CLK_Lexer (P=..., Result=...)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Lex/Preprocessor.h:2903
#2  0x000055556349ddc8 in clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Preprocessor.cpp:869
#3  0x0000555560eb0d2e in clang::Parser::ConsumeToken (this=0x55556401fe00)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Parse/Parser.h:497
#4  0x0000555560eb0af3 in clang::Parser::ConsumeAnyToken (this=0x55556401fe00,
    ConsumeCodeCompletionTok=false)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Parse/Parser.h:535
#5  0x0000555560f5819e in clang::Parser::ParseDeclarationSpecifiers (this=0x55556401fe00, DS=...,
    TemplateInfo=..., AS=clang::AS_none, DSContext=clang::Parser::DeclSpecContext::DSC_top_level,
    LateAttrs=0x0, AllowImplicitTypename=clang::ImplicitTypenameContext::Yes)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:4573
#6  0x0000555560eb2152 in clang::Parser::ParseDeclarationSpecifiers (this=0x55556401fe00, DS=...,
    TemplateInfo=..., AS=clang::AS_none, DSC=clang::Parser::DeclSpecContext::DSC_top_level,
    LateAttrs=0x0)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Parse/Parser.h:2431
#7  0x0000555560eab1b6 in clang::Parser::ParseDeclOrFunctionDefInternal (this=0x55556401fe00,
    Attrs=..., DeclSpecAttrs=..., DS=..., AS=clang::AS_none)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1143
#8  0x0000555560eaacce in clang::Parser::ParseDeclarationOrFunctionDefinition (this=0x55556401fe00,
    Attrs=..., DeclSpecAttrs=..., DS=0x0, AS=clang::AS_none)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1261
#9  0x0000555560eaa54d in clang::Parser::ParseExternalDeclaration (this=0x55556401fe00, Attrs=...,
    DeclSpecAttrs=..., DS=0x0)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1065
#10 0x0000555560ea83ac in clang::Parser::ParseTopLevelDecl (this=0x55556401fe00, Result=...,
    ImportState=@0x7fffffffaac4: clang::Sema::ModuleImportState::FirstDecl)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:755
#11 0x0000555560ea7a50 in clang::Parser::ParseFirstTopLevelDecl (this=0x55556401fe00, Result=...,
    ImportState=@0x7fffffffaac4: clang::Sema::ModuleImportState::FirstDecl)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:602
#12 0x0000555560ea315b in clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseAST.cpp:162
#13 0x000055555daab15b in clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1183
#14 0x000055555d57eda6 in clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/CodeGen/CodeGenAction.cpp:1153
#15 0x000055555daaab7c in clang::FrontendAction::Execute (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1069
#16 0x000055555d9cc61c in clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/CompilerInstance.cpp:1057
#17 0x000055555dc788f1 in clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)
    at /media/new/open_source/llvm-project/source/clang/lib/FrontendTool/ExecuteCompilerInvocation.cpp:272
#18 0x000055555a92fb9f in cc1_main (Argv=...,
    Argv0=0x7fffffffdca6 "/media/new/open_source/llvm-project/build-debug/bin/clang-18",
    MainAddr=0x55555a91ebb0 <GetExecutablePath[abi:cxx11](char const*, bool)>)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/cc1_main.cpp:294
#19 0x000055555a920372 in ExecuteCC1Tool (ArgV=..., ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:366
#20 0x000055555a91f0b4 in clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:407
#21 0x000055555a95372d in main (argc=65, argv=0x7fffffffd738)
    at /media/new/open_source/llvm-project/build-debug/tools/clang/tools/driver/clang-driver.cpp:15
"""
        accumulator.process(backtrace)

        backtrace = """#0  clang::Lexer::Lex (this=0x5555640173c0, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Lexer.cpp:3623
#1  0x0000555560eb673c in clang::Preprocessor::CLK_Lexer (P=..., Result=...)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Lex/Preprocessor.h:2903
#2  0x000055556349ddc8 in clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Preprocessor.cpp:869
#3  0x00005555634451b1 in clang::Preprocessor::PeekAhead (this=0x555563fa1190, N=1)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/PPCaching.cpp:110
#4  0x0000555560eb5700 in clang::Preprocessor::LookAhead (this=0x555563fa1190, N=0)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Lex/Preprocessor.h:1808
#5  0x0000555560eb0c8b in clang::Parser::NextToken (this=0x55556401fe00)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Parse/Parser.h:818
#6  0x0000555560f5f0f2 in clang::Parser::ParseDeclaratorInternal (this=0x55556401fe00, D=...,
    DirectDeclParser=(void (clang::Parser::*)(clang::Parser * const, clang::Declarator &)) 0x555560f601d0 <clang::Parser::ParseDirectDeclarator(clang::Declarator&)>)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:6251
#7  0x0000555560f668b7 in clang::Parser::ParseDeclarator(clang::Declarator&)::$_0::operator()() const (
    this=0x7fffffff8fa8)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:6172
#8  0x0000555560f66875 in llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>(long) (callable=140737488326568)
    at /media/new/open_source/llvm-project/source/llvm/include/llvm/ADT/STLFunctionalExtras.h:45
#9  0x000055555b35bc99 in llvm::function_ref<void ()>::operator()() const (this=0x7fffffff8f00)
    at /media/new/open_source/llvm-project/source/llvm/include/llvm/ADT/STLFunctionalExtras.h:68
#10 0x000055556106007d in clang::runWithSufficientStackSpace(llvm::function_ref<void ()>, llvm::function_ref<void ()>) (Diag=..., Fn=...)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Basic/Stack.h:46
#11 0x000055556104cb70 in clang::Sema::runWithSufficientStackSpace(clang::SourceLocation, llvm::function_ref<void ()>) (this=0x555564012cd0, Loc=..., Fn=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Sema/Sema.cpp:513
#12 0x0000555560f446c6 in clang::Parser::ParseDeclarator (this=0x55556401fe00, D=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:6171
#13 0x0000555560f500c5 in clang::Parser::ParseDeclGroup (this=0x55556401fe00, DS=...,
    Context=clang::DeclaratorContext::File, Attrs=..., DeclEnd=0x0, FRI=0x0)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:2196
#14 0x0000555560eab7dc in clang::Parser::ParseDeclOrFunctionDefInternal (this=0x55556401fe00,
    Attrs=..., DeclSpecAttrs=..., DS=..., AS=clang::AS_none)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1239
#15 0x0000555560eaacce in clang::Parser::ParseDeclarationOrFunctionDefinition (this=0x55556401fe00,
    Attrs=..., DeclSpecAttrs=..., DS=0x0, AS=clang::AS_none)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1261
#16 0x0000555560eaa54d in clang::Parser::ParseExternalDeclaration (this=0x55556401fe00, Attrs=...,
    DeclSpecAttrs=..., DS=0x0)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1065
#17 0x0000555560ea83ac in clang::Parser::ParseTopLevelDecl (this=0x55556401fe00, Result=...,
    ImportState=@0x7fffffffaac4: clang::Sema::ModuleImportState::FirstDecl)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:755
#18 0x0000555560ea7a50 in clang::Parser::ParseFirstTopLevelDecl (this=0x55556401fe00, Result=...,
    ImportState=@0x7fffffffaac4: clang::Sema::ModuleImportState::FirstDecl)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:602
#19 0x0000555560ea315b in clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseAST.cpp:162
#20 0x000055555daab15b in clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1183
#21 0x000055555d57eda6 in clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/CodeGen/CodeGenAction.cpp:1153
#22 0x000055555daaab7c in clang::FrontendAction::Execute (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1069
#23 0x000055555d9cc61c in clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/CompilerInstance.cpp:1057
#24 0x000055555dc788f1 in clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)
    at /media/new/open_source/llvm-project/source/clang/lib/FrontendTool/ExecuteCompilerInvocation.cpp:272
#25 0x000055555a92fb9f in cc1_main (Argv=...,
    Argv0=0x7fffffffdca6 "/media/new/open_source/llvm-project/build-debug/bin/clang-18",
    MainAddr=0x55555a91ebb0 <GetExecutablePath[abi:cxx11](char const*, bool)>)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/cc1_main.cpp:294
#26 0x000055555a920372 in ExecuteCC1Tool (ArgV=..., ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:366
#27 0x000055555a91f0b4 in clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:407
#28 0x000055555a95372d in main (argc=65, argv=0x7fffffffd738)
    at /media/new/open_source/llvm-project/build-debug/tools/clang/tools/driver/clang-driver.cpp:15
"""
        accumulator.process(backtrace)

        backtrace = """#0  clang::Lexer::Lex (this=0x5555640173c0, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Lexer.cpp:3623
#1  0x0000555560eb673c in clang::Preprocessor::CLK_Lexer (P=..., Result=...)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Lex/Preprocessor.h:2903
#2  0x000055556349ddc8 in clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Preprocessor.cpp:869
#3  0x0000555563444f55 in clang::Preprocessor::CachingLex (this=0x555563fa1190, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/PPCaching.cpp:63
#4  0x000055556344585d in clang::Preprocessor::CLK_CachingLexer (P=..., Result=...)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Lex/Preprocessor.h:2909
#5  0x000055556349ddc8 in clang::Preprocessor::Lex (this=0x555563fa1190, Result=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Lex/Preprocessor.cpp:869
#6  0x0000555560eb10d8 in clang::Parser::ConsumeParen (this=0x55556401fe00)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Parse/Parser.h:608
#7  0x0000555560fa7816 in clang::Parser::isCXXFunctionDeclarator (this=0x55556401fe00,
    IsAmbiguous=0x7fffffff7e67, AllowImplicitTypename=clang::ImplicitTypenameContext::No)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseTentative.cpp:1987
#8  0x0000555560f61ae1 in clang::Parser::ParseDirectDeclarator (this=0x55556401fe00, D=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:6770
#9  0x0000555560f5f7b0 in clang::Parser::ParseDeclaratorInternal (this=0x55556401fe00, D=...,
    DirectDeclParser=(void (clang::Parser::*)(clang::Parser * const, clang::Declarator &)) 0x555560f601d0 <clang::Parser::ParseDirectDeclarator(clang::Declarator&)>)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:6313
#10 0x0000555560f668b7 in clang::Parser::ParseDeclarator(clang::Declarator&)::$_0::operator()() const (
    this=0x7fffffff8fa8)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:6172
#11 0x0000555560f66875 in llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>(long) (callable=140737488326568)
    at /media/new/open_source/llvm-project/source/llvm/include/llvm/ADT/STLFunctionalExtras.h:45
#12 0x000055555b35bc99 in llvm::function_ref<void ()>::operator()() const (this=0x7fffffff8f00)
    at /media/new/open_source/llvm-project/source/llvm/include/llvm/ADT/STLFunctionalExtras.h:68
#13 0x000055556106007d in clang::runWithSufficientStackSpace(llvm::function_ref<void ()>, llvm::function_ref<void ()>) (Diag=..., Fn=...)
    at /media/new/open_source/llvm-project/source/clang/include/clang/Basic/Stack.h:46
#14 0x000055556104cb70 in clang::Sema::runWithSufficientStackSpace(clang::SourceLocation, llvm::function_ref<void ()>) (this=0x555564012cd0, Loc=..., Fn=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Sema/Sema.cpp:513
#15 0x0000555560f446c6 in clang::Parser::ParseDeclarator (this=0x55556401fe00, D=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:6171
#16 0x0000555560f500c5 in clang::Parser::ParseDeclGroup (this=0x55556401fe00, DS=...,
    Context=clang::DeclaratorContext::File, Attrs=..., DeclEnd=0x0, FRI=0x0)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseDecl.cpp:2196
#17 0x0000555560eab7dc in clang::Parser::ParseDeclOrFunctionDefInternal (this=0x55556401fe00,
    Attrs=..., DeclSpecAttrs=..., DS=..., AS=clang::AS_none)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1239
#18 0x0000555560eaacce in clang::Parser::ParseDeclarationOrFunctionDefinition (this=0x55556401fe00,
    Attrs=..., DeclSpecAttrs=..., DS=0x0, AS=clang::AS_none)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1261
#19 0x0000555560eaa54d in clang::Parser::ParseExternalDeclaration (this=0x55556401fe00, Attrs=...,
    DeclSpecAttrs=..., DS=0x0)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:1065
#20 0x0000555560ea83ac in clang::Parser::ParseTopLevelDecl (this=0x55556401fe00, Result=...,
    ImportState=@0x7fffffffaac4: clang::Sema::ModuleImportState::FirstDecl)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:755
#21 0x0000555560ea7a50 in clang::Parser::ParseFirstTopLevelDecl (this=0x55556401fe00, Result=...,
    ImportState=@0x7fffffffaac4: clang::Sema::ModuleImportState::FirstDecl)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/Parser.cpp:602
#22 0x0000555560ea315b in clang::ParseAST (S=..., PrintStats=false, SkipFunctionBodies=false)
    at /media/new/open_source/llvm-project/source/clang/lib/Parse/ParseAST.cpp:162
#23 0x000055555daab15b in clang::ASTFrontendAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1183
#24 0x000055555d57eda6 in clang::CodeGenAction::ExecuteAction (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/CodeGen/CodeGenAction.cpp:1153
#25 0x000055555daaab7c in clang::FrontendAction::Execute (this=0x555563f9d9c0)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/FrontendAction.cpp:1069
#26 0x000055555d9cc61c in clang::CompilerInstance::ExecuteAction (this=0x555563f9b460, Act=...)
    at /media/new/open_source/llvm-project/source/clang/lib/Frontend/CompilerInstance.cpp:1057
#27 0x000055555dc788f1 in clang::ExecuteCompilerInvocation (Clang=0x555563f9b460)
    at /media/new/open_source/llvm-project/source/clang/lib/FrontendTool/ExecuteCompilerInvocation.cpp:272
#28 0x000055555a92fb9f in cc1_main (Argv=...,
    Argv0=0x7fffffffdca6 "/media/new/open_source/llvm-project/build-debug/bin/clang-18",
    MainAddr=0x55555a91ebb0 <GetExecutablePath[abi:cxx11](char const*, bool)>)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/cc1_main.cpp:294
#29 0x000055555a920372 in ExecuteCC1Tool (ArgV=..., ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:366
#30 0x000055555a91f0b4 in clang_main (Argc=65, Argv=0x7fffffffd738, ToolContext=...)
    at /media/new/open_source/llvm-project/source/clang/tools/driver/driver.cpp:407
#31 0x000055555a95372d in main (argc=65, argv=0x7fffffffd738)
    at /media/new/open_source/llvm-project/build-debug/tools/clang/tools/driver/clang-driver.cpp:15
"""
        accumulator.process(backtrace)
        accumulator.hide_until_func = "clang::ParseAST"

        result_dot_code = accumulator.process("")

        expected_dot_code = """digraph Backtrace {
    node [shape=box]
    "clang::ParseAST" -> "clang::Parser::Initialize"
    "clang::Parser::Initialize" -> "clang::Parser::ConsumeToken"
    "clang::Parser::ConsumeToken" -> "clang::Preprocessor::Lex"
    "clang::Preprocessor::Lex" -> "clang::Preprocessor::CLK_Lexer"
    "clang::Preprocessor::CLK_Lexer" -> "clang::Lexer::Lex"
    "clang::Preprocessor::Lex" -> "clang::Preprocessor::CLK_CachingLexer"
    "clang::Preprocessor::CLK_CachingLexer" -> "clang::Preprocessor::CachingLex"
    "clang::Preprocessor::CachingLex" -> "clang::Preprocessor::Lex"
    "clang::ParseAST" -> "clang::Parser::ParseFirstTopLevelDecl"
    "clang::Parser::ParseFirstTopLevelDecl" -> "clang::Parser::ParseTopLevelDecl"
    "clang::Parser::ParseTopLevelDecl" -> "clang::Parser::ParseExternalDeclaration"
    "clang::Parser::ParseExternalDeclaration" -> "clang::Parser::ParseDeclarationOrFunctionDefinition"
    "clang::Parser::ParseDeclarationOrFunctionDefinition" -> "clang::Parser::ParseDeclOrFunctionDefInternal"
    "clang::Parser::ParseDeclOrFunctionDefInternal" -> "clang::Parser::ParseDeclarationSpecifiers"
    "clang::Parser::ParseDeclarationSpecifiers" -> "clang::Parser::ConsumeAnyToken"
    "clang::Parser::ConsumeAnyToken" -> "clang::Parser::ConsumeToken"
    "clang::Parser::ParseDeclarationSpecifiers" -> "clang::Parser::ParseDeclarationSpecifiers"
    "clang::Parser::ParseDeclOrFunctionDefInternal" -> "clang::Parser::ParseDeclGroup"
    "clang::Parser::ParseDeclGroup" -> "clang::Parser::ParseDeclarator"
    "clang::Parser::ParseDeclarator" -> "clang::Parser::ParseDeclaratorInternal"
    "clang::Parser::ParseDeclaratorInternal" -> "clang::Parser::NextToken"
    "clang::Parser::NextToken" -> "clang::Preprocessor::LookAhead"
    "clang::Preprocessor::LookAhead" -> "clang::Preprocessor::PeekAhead"
    "clang::Preprocessor::PeekAhead" -> "clang::Preprocessor::Lex"
    "clang::Parser::ParseDeclaratorInternal" -> "clang::Parser::ParseDirectDeclarator"
    "clang::Parser::ParseDirectDeclarator" -> "clang::Parser::isCXXFunctionDeclarator"
    "clang::Parser::isCXXFunctionDeclarator" -> "clang::Parser::ConsumeParen"
    "clang::Parser::ConsumeParen" -> "clang::Preprocessor::Lex"
    "clang::Parser::ParseDeclarator" -> "clang::Sema::runWithSufficientStackSpace"
    "clang::Sema::runWithSufficientStackSpace" -> "clang::runWithSufficientStackSpace"
    "clang::runWithSufficientStackSpace" -> "llvm::function_ref<void ()>::operator()"
    "llvm::function_ref<void ()>::operator()" -> "llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>"
    "llvm::function_ref<void ()>::callback_fn<clang::Parser::ParseDeclarator(clang::Declarator&)::$_0>" -> "clang::Parser::ParseDeclarator"
}"""

        self.assertEqual(result_dot_code, expected_dot_code)


if __name__ == "__main__":
    unittest.main()
