from _common import *

page = dict(
    slug="environmental-green-plumbers", kind="core", crumb="Green plumbing",
    title="Water & Energy Efficient Plumbing Gold Coast | Moyle",
    description='Water and energy efficient plumbing for Gold Coast and Logan homes: efficient fixtures, leak control, heat pump hot water. Call (07) 3807 7327.',
    h1="Water and energy efficient plumbing",
    eyebrow="Green plumbing",
    intro="<p>Water and energy efficient plumbing is mostly practical, not exotic. The biggest wins in any Gold Coast house are stopping leaks, choosing fixtures that use less water without feeling weaker, and picking a hot water system that does not burn electricity. Moyle Plumbing &amp; Gasfitting builds those choices into everyday repairs and replacements across the northern Gold Coast and Logan.</p>",
    breadcrumb=[],
    body=sec("""
<h2>Where a household's water actually goes</h2>
<p>Showers, toilets, washing machines and the garden take most of it, and leaks quietly take more than people expect. That means the order of priorities is clear:</p>
<ol class="steps">
<li><strong>Find and fix leaks.</strong> A running cistern or a weeping pipe under the slab wastes more than any fixture upgrade saves. The ten-minute meter test on the """ + L("leak-repairs", "leak detection page") + """ is the place to start.</li>
<li><strong>Shower heads and taps.</strong> A quality efficient shower head feels fine and uses far less water. Aerators on basin and kitchen taps cost almost nothing.</li>
<li><strong>Toilets.</strong> Replacing a single-flush suite with a modern dual-flush cuts one of the biggest indoor uses. See """ + L("toilets", "toilet replacement") + """.</li>
<li><strong>Hot water.</strong> Heating water is one of the largest energy uses in the home; the system choice matters more than any other single decision.</li>
<li><strong>Rainwater.</strong> A tank plumbed to toilets, laundry and garden takes real demand off the mains.</li>
</ol>
""") + soft("""
<h2>Hot water: the energy decision</h2>
<p>A plain electric storage unit on a standard tariff is the most expensive way to heat water. A heat pump uses a fraction of the electricity and suits the Gold Coast climate. Solar with a booster uses less again where the roof allows. Gas sits in between and depends on supply. When a unit fails, the replacement is the moment to change, and rebates often help. Each type is weighed on the """ + L("hot-water", "hot water page") + """. Whatever the system, a correctly set """ + L("hot-water-tempering-valves", "tempering valve") + """ and well-insulated pipes stop heat being wasted on the way to the tap.</p>
<h2>Rainwater and greywater</h2>
<p>A rainwater tank on a suburban block is most useful plumbed to the toilets, the washing machine and the garden, with an automatic changeover to mains when it runs dry. On acreage it is the whole supply, and filtration and pump choice decide how well it works; see """ + L("pumps", "pumps") + """ and """ + L("water-filter-installation", "water filters") + """. Greywater reuse is possible but regulated, and we advise honestly on whether a system suits the property.</p>
""") + sec("""
<h2>Efficiency for rentals</h2>
<p>Queensland's water efficiency rules for rentals set flow limits for taps and showers and require dual-flush toilets before an owner can pass on water charges. Meeting them saves water for the tenant and money for the owner; see """ + L("water-compliancy", "water compliance") + """.</p>
<h2>Small habits that add up</h2>
<ul class="checks">
<li>Fix a dripping tap the week it starts, not the year.</li>
<li>Check the meter once a season with everything off.</li>
<li>Insulate exposed hot water pipes, especially the first metres from the unit.</li>
<li>Set the tempering valve properly rather than turning the tank thermostat down below safe levels.</li>
<li>Choose fixtures with a high water efficiency rating when replacing them.</li>
</ul>
<p>Water escaping right now is an urgent matter, not an efficiency one; the """ + H("running leak emergency page") + """ page walks you through it. Everything else here is part of the everyday """ + L("general-plumbing-maintenance", "plumbing maintenance") + """ we do. The family has run Moyle Plumbing &amp; Gasfitting since 1983; there is more on the """ + M("Moyle Plumbing website") + """.</p>
"""),
    faqs=[
        ("Will an efficient shower head feel weak?",
         "<p>Modern designs mix air with the water and feel much the same as older heads at a fraction of the flow. Cheap restrictors on old heads are what give efficiency a bad name.</p>"),
        ("Is a heat pump noisy?",
         "<p>It has a fan, so it makes a sound similar to a small air conditioner while running. Siting it away from bedroom windows and neighbours' living areas deals with it.</p>"),
        ("Can I plumb a rainwater tank into the house myself?",
         "<p>Connecting a tank to the internal plumbing is licensed work in Queensland because of the backflow risk to the mains. Garden-only tanks are simpler, but anything feeding the house needs a plumber.</p>"),
    ],
    related=[
        ("hot-water", "Hot water systems"),
        ("water-compliancy", "Water compliance"),
        ("leak-repairs", "Leak detection"),
        ("pumps", "Pumps"),
        ("water-filter-installation", "Water filters"),
        ("about-us", "About us"),
    ],
)
