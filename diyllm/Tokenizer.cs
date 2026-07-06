using System.Text.RegularExpressions;

namespace diyllm
{
    public class Tokenizer
    {
        private readonly Dictionary<string, int> _strToInt = [];
        private readonly Dictionary<int, string> _intToStr = [];

        private int _nextId = 0;

        public IReadOnlyDictionary<string, int> Vocabulary => _strToInt;

        public List<int> Encode(string text)
        {
            // Split on punctuation, "--", or whitespace while keeping delimiters.
            var tokens = Regex.Split(text, @"([,.?_!""()']|--|\s)")
                .Select(s => s.Trim())
                .Where(s => !string.IsNullOrWhiteSpace(s));

            var ids = new List<int>();

            foreach (var token in tokens)
            {
                if (!_strToInt.TryGetValue(token, out int id))
                {
                    id = _nextId++;
                    _strToInt[token] = id;
                    _intToStr[id] = token;
                }

                ids.Add(id);
            }

            return ids;
        }

        public string Decode(IEnumerable<int> ids)
        {
            var tokens = ids.Select(id =>
            {
                if (!_intToStr.TryGetValue(id, out var token))
                    throw new ArgumentException($"Unknown token ID: {id}");

                return token;
            });

            var text = string.Join(" ", tokens);

            // Remove spaces before punctuation.
            return Regex.Replace(text, @"\s+([,.?!""()'])", "$1");
        }
    }
}