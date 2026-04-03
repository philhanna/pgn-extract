# Call Tree: main() in main.c

## main() [main.c:170]

```
main() [main.c:170]
├── init_default_global_state() [main.c:176]
│   └── set_output_line_length() [output.c:139]
│
├── init_game_header() [main.c:178 → grammar.c:101]
│   └── malloc_or_die()
│
├── init_tag_lists() [main.c:180 → lists.c:88]
│   └── malloc_or_die()
│
├── init_hashtab() [main.c:182 → map.c:173]
│
├── init_lex_tables() [main.c:184 → lex.c:239]
│   └── init_list_of_known_tags() [lex.c:109]
│       └── malloc_or_die()
│
├── process_argument() [main.c:203,209,217,228,288,322,330,369,373 → argsfile.c:547]
│   ├── skip_leading_spaces() [argsfile.c:107]
│   ├── must_open_file() [grammar.c:135]
│   │   └── fopen()
│   ├── copy_string() [apply.c:171]
│   │   └── malloc_or_die()
│   ├── getenv()
│   ├── initEcoTable() [eco.c:139]
│   │   └── malloc_or_die()
│   ├── set_output_line_length() [output.c:139]
│   ├── set_move_bounds() [argsfile.c:67]
│   ├── which_output_format() [output.c:152]
│   ├── read_args_file() [argsfile.c:302]
│   │   ├── read_line()
│   │   ├── stringcompare()
│   │   ├── process_argument() [RECURSIVE]
│   │   └── fclose()
│   ├── read_tag_file() [taglines.c:45]
│   │   ├── read_line()
│   │   └── extract_tag_argument() [lists.c:359]
│   ├── read_tag_roster_file() [taglines.c:78]
│   ├── add_filename_list_from_file() [lex.c:1403]
│   │   └── read_line()
│   ├── add_textual_variations_from_file() [moves.c:239]
│   ├── add_positional_variations_from_file() [moves.c:334]
│   ├── build_endings() [end.c:817]
│   │   └── process_material_description() [end.c:793]
│   ├── suppress_tag() [lex.c:224]
│   │   ├── identify_tag() [lex.c:739]
│   │   └── make_new_tag() [lex.c:176]
│   │       └── copy_string() [apply.c:171]
│   ├── add_fen_pattern() [fenmatcher.c:93]
│   ├── save_polyglot_hashcode() [apply.c:2551]
│   └── output_file_suffix() [output.c:215]
│
├── process_long_form_argument() [main.c:248 → argsfile.c:1026]
│   ├── stringcompare()
│   ├── process_argument() [RECURSIVE back to argsfile.c:547]
│   ├── suppress_tag() [lex.c:224]
│   ├── add_fen_pattern() [fenmatcher.c:93]
│   ├── set_move_bounds() [argsfile.c:67]
│   └── process_material_description() [end.c:793]
│
├── add_filename_to_source_list() [main.c:386 → lex.c:1433]
│   ├── access()
│   ├── malloc_or_die()
│   ├── realloc_or_die()
│   └── copy_string() [apply.c:171]
│
├── init_duplicate_hash_table() [main.c:407 → hashing.c:281]
│   └── malloc_or_die()
│
├── open_eco_file() [main.c:411 → lex.c:1522]
│   └── open_input() [lex.c]
│       └── fopen()
│
├── open_first_file() [main.c:426 → lex.c:1545]
│   ├── open_input_file() [lex.c:1534]
│   │   └── open_input() [lex.c]
│   │       └── fopen()
│   └── input_file_name() [lex.c:1558]
│
├── reset_line_number() [main.c:415 → lex.c:1683]
│
├── yyparse() [main.c:414,430 → grammar.c:1549]
│   ├── setup_for_new_game() [grammar.c:894]
│   │   └── restart_lex_for_new_game() [lex.c:1273]
│   ├── skip_to_next_game() [lex.c:1223]
│   │   ├── skip_token() [lex.c:1204]
│   │   ├── next_token() [lex.c:1188]
│   │   └── free_string_list() [grammar.c:915]
│   ├── parse_opt_game_list() [grammar.c:384]
│   │   ├── parse_game() [grammar.c:422]
│   │   │   ├── skip_to_next_game() [lex.c:1223]
│   │   │   ├── parse_opt_comment_list() [grammar.c:728]
│   │   │   ├── get_line_number() [lex.c:1676]
│   │   │   ├── parse_opt_tag_list() [grammar.c:512]
│   │   │   │   ├── parse_tag() [grammar.c:591]
│   │   │   │   └── next_token() [lex.c:1188]
│   │   │   ├── parse_move_list() [grammar.c:645]
│   │   │   ├── parse_result() [grammar.c:874]
│   │   │   ├── check_result() [grammar.c:182]
│   │   │   ├── append_comment() [grammar.c:1045]
│   │   │   └── report_details() [grammar.c:152]
│   │   ├── deal_with_game() [grammar.c:1163]
│   │   │   ├── consistent_FEN_tags()
│   │   │   ├── check_tag_details_not_ECO()
│   │   │   ├── check_setup_tag()
│   │   │   ├── check_duplicate_setup() [hashing.c:567]
│   │   │   ├── apply_move_list()
│   │   │   ├── check_move_bounds()
│   │   │   ├── check_for_odds()
│   │   │   ├── check_textual_variations()
│   │   │   ├── check_for_material_match()
│   │   │   ├── check_for_piece_count_match()
│   │   │   ├── check_for_only_checkmate()
│   │   │   ├── check_for_only_repetition() [hashing.c:112]
│   │   │   ├── check_ECO_tag()
│   │   │   ├── check_for_comments()
│   │   │   ├── previous_occurance() [hashing.c:457]
│   │   │   │   ├── previous_virtual_occurance() [hashing.c:368]
│   │   │   │   │   ├── retrieve_virtual_entry() [hashing.c:320]
│   │   │   │   │   └── write_virtual_entry() [hashing.c:342]
│   │   │   │   └── input_file_name() [lex.c:1558]
│   │   │   ├── in_game_number_range()
│   │   │   ├── select_output_file()
│   │   │   ├── print_str()
│   │   │   ├── terminate_line()
│   │   │   └── output_game()
│   │   ├── deal_with_ECO_line() [grammar.c:1503]
│   │   ├── free_tags() [grammar.c:901]
│   │   ├── free_move_list()
│   │   │   └── free_move() [RECURSIVE]
│   │   └── setup_for_new_game() [grammar.c:894]
│
├── clear_duplicate_hash_table() [main.c:444 → hashing.c:307]
│   ├── fclose()
│   └── unlink()
│
└── fclose() [main.c:452]
```

## Notes

- **`process_argument()` ↔ `process_long_form_argument()`**: Mutual recursion — long-form arguments delegate back to `process_argument`, and `read_args_file()` also calls `process_argument` recursively.
- **`next_token()` [lex.c:1188]**: Large internal lexer function with complex branching for all token types; not expanded here.
- **`apply_move_list()`**: Highly complex move validation and board state management; not expanded here.
- **`free_move()` [grammar.c]**: Recursively frees a linked list of moves.
- **`yyparse()`**: Generated by yacc/bison; the structure above reflects the grammar rules as implemented in `grammar.c`.

## File Distribution

| File | Role |
|------|------|
| `grammar.c` | Parsing, game processing, tag handling |
| `lex.c` | Lexical analysis, input file management |
| `argsfile.c` | Command-line argument processing |
| `hashing.c` | Duplicate detection, position hashing |
| `output.c` | Output formatting |
| `apply.c` | Move application, string utilities |
| `end.c` | Endgame material matching |
| `moves.c` | Move variation handling |
| `taglines.c` | Tag file reading |
| `lists.c` | Tag list management |
| `fenmatcher.c` | FEN position matching |
| `eco.c` | ECO classification |
| `map.c` | Hash table initialisation |
