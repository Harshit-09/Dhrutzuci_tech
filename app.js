const express = require('express')
var bodyParser = require("body-parser");
const app = express()
app.listen(3000)

app.use(bodyParser.json());

app.post("/find_symbols_in_names", (req, res) => {
  var chemicals = req.body.chemicals;
  var symbols = req.body.symbols;
  var out = [];

  chemicals.forEach(chemical => {
    symbols.forEach((symbol, index) => {

      var startIndex = chemical.indexOf(symbol);

      if (startIndex != -1) {

        var endIndex = startIndex + symbol.length;
        
        symbols.splice(index, 1);

        var output = [
          chemical.slice(0, startIndex),
          "[",
          symbol,
          "]",
          chemical.slice(endIndex, chemical.length),
        ].join("");

        out.push(output);
      }
    });
  });

  res.send({
    result: out.join(", "),
  });
});



