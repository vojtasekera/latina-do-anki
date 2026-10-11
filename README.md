## Slovíčka 
V Anki stačí importovat do dvou polí, latinsky a česky, a třetí sloupec hodit do tagů, pomocí kterých se dá vytvořit filtrovaný balíček, filtr si pak měním každý týden podle potřeby. Viz filtr třeba takto: `"deck:Latina III" tag:3.2`.

## Slovesné stupnice

<table>
<tr>
<td valign="top">
Slovesa bude třeba importovat s políčky na víc řádků a potom je problém se zarovnáním odpovědi, proto musíme dodat do definice karet skript na parsování.
</td>
<td valign="top">
<img src="tabulka se slovesy.png" align="right" width="1000" alt="Anki card">
</td>
</tr>
</table>


### Šablony pro rub a líc
<table>
<tr>
<td valign="top" >

V prvních třech řádcích si nastavte svá jména polí a do `data-hide=` dosaďte, kterou část chcete zakrýt: `"cz"`, `"la"` nebo `""`.

</td>
<td valign="top" width= 200 >

|  | rub                        | líc  |
|--------|------------------------------|--------|
| Karta 1     | "cz"   | ""  |
| Karta 2  | "la"   | ""  |

</td>
</tr>
</table>



```html
<div id="la-src" style="display:none">{{latin}}</div>
<div id="cz-src" style="display:none">{{czech}}</div>
<table class="verbs" id="verbs" data-hide="cz"></table>

<script>
(() => {
  const SPLIT_RUNS = true;
  const lines = id => document.getElementById(id).innerHTML
    .split(/<br\s*\/?>|\n/i).map(s => s.trim()).filter(s => s);
  let la = lines('la-src'), cz = lines('cz-src');
  if (SPLIT_RUNS) {
    const la2 = la.flatMap(l => l.split('; ')), cz2 = cz.flatMap(l => l.split('; '));
    if (la2.length === cz2.length) { la = la2; cz = cz2; }
  }
  const t = document.getElementById('verbs');
  const hideCol = t.dataset.hide;
  const cell = (col, text) =>
    `<td class="${col}"${hideCol === col ? ' style="visibility:hidden"' : ''}>${text}</td>`;
  t.innerHTML = la.map((l, i) =>
    `<tr>${cell('la', l)}${cell('cz', cz[i] || '')}</tr>`).join('');
})();
</script>
</script>
```
```css
<!-- STYL -->
.card {
 font-family: arial;
 font-size: 20px;
 text-align: left;
 color: black;
 background-color: white;
}
td {text-align: left;}
table{margin: 0px auto;}
.num { text-align: center; font-weight: bold; margin-bottom: 10px; }
.src { display: none; }
table.verbs { border-collapse: collapse; margin: 0 auto; }
table.verbs td { padding: 5px 12px; vertical-align: top; border-bottom: 1px solid #ddd; }
td.cz { color: #444; }
td.hide { visibility: hidden; }
.nightMode td.cz, .night_mode td.cz { color: #bbb; }
.nightMode table.verbs td, .night_mode table.verbs td { border-color: #444; }
```