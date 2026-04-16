#!/usr/bin/env python3
from simulstreaming_whisper import simulwhisper_args, simul_asr_factory
from simulstreaming.whisper.whisper_streaming.whisper_server import main_server


def main():
    main_server(simul_asr_factory, add_args=simulwhisper_args)


if __name__ == "__main__":
    main()