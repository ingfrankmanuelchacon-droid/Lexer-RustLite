lexer grammar RustLite;

// --- 1. Palabras Reservadas de Rust ---
FN      : 'fn';
LET     : 'let';
MUT     : 'mut';
RETURN  : 'return';
IF      : 'if';
ELSE    : 'else';
PRINT   : 'println!';

// --- 2. Tipos de Datos ---
TYPE_I32  : 'i32';
TYPE_BOOL : 'bool';

// --- 3. Operadores y Símbolos ---
ARROW   : '->';
ASSIGN  : '=';
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
SEMI    : ';';
COLON   : ':';
COMMA   : ',';

// --- 4. Identificadores y Literales ---
// ID: Empieza con letra o _, sigue con letras, numeros o _
ID      : [a-zA-Z_] [a-zA-Z0-9_]*; 

// INT: Uno o más dígitos
INT     : [0-9]+;

// --- 5. Ignorar basura ---
// WS: Salta espacios, tabs y saltos de línea
WS      : [ \t\r\n]+ -> skip;

// COMMENT: Salta comentarios //
COMMENT : '//' ~[\r\n]* -> skip;