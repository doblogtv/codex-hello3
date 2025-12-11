"""Play a 1 kHz tone for one second on Windows."""
import winsound


def main() -> None:
    frequency_hz = 1000
    duration_ms = 1000
    winsound.Beep(frequency_hz, duration_ms)


if __name__ == "__main__":
    main()
