class ConsoleLoggerAdapter:
    def log(self, message: str):
        # Logic from verbosity handling in argsfile.c
        print(f"[LOG]: {message}")