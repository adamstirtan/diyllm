using diyllm;

var tokenizer = new Tokenizer();

var ids = tokenizer.Encode("Hello, world!");
Console.WriteLine(string.Join(", ", ids));
// Output: 0, 1, 2, 3

Console.WriteLine(tokenizer.Decode(ids));
// Output: Hello, world!

var moreIds = tokenizer.Encode("Hello again!");
Console.WriteLine(string.Join(", ", moreIds));
// Output: 0, 4, 3