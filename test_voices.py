#!/usr/bin/env python3
"""
Test script to check available TTS voices and their quality
"""
import pyttsx3

def test_voices():
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        print("Available voices:")
        for i, voice in enumerate(voices):
            print(f"{i}: {voice.name} (ID: {voice.id})")
            print(f"   Languages: {voice.languages}")
            print(f"   Gender: {voice.gender if hasattr(voice, 'gender') else 'Unknown'}")
            print()
        
        # Test with different settings
        print("Testing voice clarity with different settings...")
        
        test_text = "Access granted. Welcome."
        
        # Test 1: Default settings
        print("Test 1: Default settings")
        engine.setProperty('rate', 140)
        engine.setProperty('volume', 0.9)
        if voices:
            engine.setProperty('voice', voices[0].id)
        engine.say(test_text)
        engine.runAndWait()
        
        # Test 2: If multiple voices available, try the second one
        if len(voices) > 1:
            print("Test 2: Alternative voice")
            engine.setProperty('voice', voices[1].id)
            engine.say(test_text)
            engine.runAndWait()
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_voices()
