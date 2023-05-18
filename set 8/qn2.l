%{
    /*program*/
%}
Oct[o][0-7]+
Hex 0x[0-9a-fA-F]+
%%
{Hex} printf("This is Hexadecimal number");
{Oct} printf("This is an Octal number");
%%
main()
{
yylex();
}
int yywrap()
{
return 1;
}
