using System;
using System.Collections.Generic;
using System.Text;

namespace diyllm;

public class Tokenizer
{
    private string[] _vocabulary;

    public Tokenizer(string input)
    {
        var split = input.Split([' ', '\n', '\r', '\t', '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '"', '\''], StringSplitOptions.RemoveEmptyEntries);

        _vocabulary = split;
    }

    public void Encode(string text)
    {
        // Implement encoding logic here

    }

    public void Decode(string text)
    {
    }
}
