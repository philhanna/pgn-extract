import argparse
import sys
from pgn.domain.chess_engine import ChessEngine
from pgn.domain.duplicate_detector import DuplicateDetector
from pgn.adapters.file_pgn_adapter import FilePGNAdapter
from pgn.application.app_service import PGNProcessor

def main():
    parser = argparse.ArgumentParser(
        description="pgn-extract: a Portable Game Notation (PGN) manipulator.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Mapping flags from argsfile.c
    parser.add_argument("-o", "--output", help="Write extracted games to outputfile (existing contents lost)")
    parser.add_argument("-a", "--append", help="Append extracted games to outputfile")
    parser.add_argument("-l", "--log", help="Save the diagnostics in logfile rather than using stderr")
    parser.add_argument("-L", "--appendlog", help="Append all diagnostics to logfile, rather than overwriting")
    
    # Duplicate handling (hashing.c logic)
    parser.add_argument("-D", "--noduplicates", action="store_true", help="Don't output duplicate games")
    parser.add_argument("-d", "--duplicates", help="Write duplicate games to the specified file")
    
    # Move/Ply Bounds (apply.c logic)
    parser.add_argument("-b", "--movebounds", help="Restricted bounds on moves, e.g., 'lnum', 'unum', or 'num'")
    parser.add_argument("-p", "--plybounds", help="Restricted bounds on ply, e.g., 'lnum', 'unum', or 'num'")
    
    # Extraction Criteria (moves.c logic)
    parser.add_argument("-M", "--checkmate", action="store_true", help="Match only games which end in checkmate")
    parser.add_argument("-V", "--novars", action="store_true", help="Don't include variations in the output")
    parser.add_argument("-N", "--nonags", action="store_true", help="Don't include NAGs in the output")
    parser.add_argument("-C", "--nocomments", action="store_true", help="Don't include comments in the output")
    
    # Output Formats (typedef.h logic)
    parser.add_argument("--json", action="store_true", help="Output the game in JSON format")
    parser.add_argument("-W", "--format", choices=['san', 'uci', 'epd', 'fen'], default='san', help="Specify output format")
    
    # Special rules
    parser.add_argument("--50", dest="fifty_move_rule", action="store_true", help="Only output games with 50 moves no capture/pawn move")
    parser.add_argument("--75", dest="seventy_five_move_rule", action="store_true", help="Only output games with 75 moves no capture/pawn move")
    
    # Positional/Source
    parser.add_argument("files", nargs="*", help="PGN source files to process")
    parser.add_argument("--version", action="version", version="pgn-extract-py v0.1 (Port of v26-02)")

    args = parser.parse_args()

    if not args.files:
        parser.print_help()
        sys.exit(1)

    # 1. Initialize Domain Logic (The Hexagon)
    engine = ChessEngine()
    detector = DuplicateDetector()

    # 2. Initialize Adapters (Infrastructure)
    # In a full implementation, we would pass 'args' to a configuration object
    # that the Engine and Detector use to set internal state (like GlobalState in C).
    repo = FilePGNAdapter()

    # 3. Initialize the Application Service (Orchestrator)
    processor = PGNProcessor(repo, engine, detector)

    # 4. Execution
    try:
        for pgn_file in args.files:
            if args.log or args.appendlog:
                print(f"Processing {pgn_file}...", file=sys.stderr)
            
            processor.process_extraction(pgn_file)
            
    except FileNotFoundError as e:
        print(f"Error: Could not open file - {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()