from _common import *

page = dict(
    slug="hot-water-repairs-brisbane-southside", kind="suburb", crumb="Hot water repairs Brisbane southside",
    title="Hot Water Repairs Brisbane Southside | Moyle Plumbing",
    description="Hot water repairs across Brisbane's southside: fault-finding on electric, gas, solar and heat pump units, parts on the van. Call (07) 3807 7327.",
    h1="Hot water repairs, Brisbane southside",
    eyebrow="Fault-finding and repair",
    intro="""<p>Hot water repairs on Brisbane's southside are about diagnosis first. Most units that stop working are fixable, and the trick is knowing which part has failed before ordering anything. Moyle Plumbing &amp; Gasfitting fault-finds and repairs every common type of unit from Eight Mile Plains to Springwood, with common parts on the van. Choosing a new system is a separate page: """ + L("hot-water-systems-brisbane-southside", "hot water systems Brisbane southside") + """.</p>""",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Hot water repairs on Brisbane's southside", area="Brisbane Southside"),
    body=sec("""
<h2>Symptom to likely fault</h2>
<table>
<thead><tr><th>Symptom</th><th>Electric storage</th><th>Gas storage</th><th>Continuous flow</th></tr></thead>
<tbody>
<tr><td>No hot water at all</td><td>Tripped breaker, failed element or thermostat</td><td>Pilot out, thermocouple, gas valve</td><td>Error code, no power, no gas, flow sensor</td></tr>
<tr><td>Lukewarm only</td><td>One of two elements failed, thermostat low</td><td>Thermostat, burner partly blocked</td><td>Undersized gas line, scaled heat exchanger</td></tr>
<tr><td>Runs out quickly</td><td>Lower element failed, tempering valve passing cold</td><td>Dip tube failed, tempering valve</td><td>Unit too small for the demand</td></tr>
<tr><td>Water at the base</td><td>Tank rusted through, or a valve leaking</td><td>Same</td><td>Heat exchanger or fittings</td></tr>
<tr><td>Relief valve running</td><td>Valve failed or pressure too high</td><td>Same</td><td>Not applicable</td></tr>
<tr><td>Breaker trips repeatedly</td><td>Element earth fault; stop resetting it</td><td colspan="2">Not applicable</td></tr>
</tbody>
</table>
""" + callout("<p><strong>Water and power:</strong> if the unit is leaking, cut the power at the switchboard before approaching it, then close its cold water inlet tap. Never reset a breaker that keeps tripping on a leaking unit.</p>", warn=True) + """
""") + soft("""
<h2>What a repair visit involves</h2>
<ol class="steps">
<li>Confirm power and supply: breaker, tariff timer, gas supply, isolation taps.</li>
<li>Test the failed component rather than guess: elements and thermostats with a meter, gas valves and thermocouples by observation and test, error codes against the manufacturer's chart.</li>
<li>Inspect the tank for corrosion and the valves for discharge, so we can tell you whether the unit is worth repairing.</li>
<li>Quote the repair as a fixed figure, with a replacement figure alongside when the unit is nearly done.</li>
<li>Repair, refill, purge air, check the tempering valve outlet temperature and test the relief valve.</li>
</ol>
<p>Parts we carry include elements, thermostats, relief valves, tempering valves, thermocouples and common continuous flow components. Model-specific parts are ordered and fitted on a second visit.</p>
""") + sec("""
<h2>Southside homes and their units</h2>
<p>Brick houses through Eight Mile Plains, Rochedale South and Springwood mostly run electric tanks on outside walls, many on an off-peak circuit whose timer confuses diagnosis if you do not know it is there. Townhouse complexes favour compact units, electric or gas instantaneous. Solar systems from the rebate years now need pump, controller and booster attention. Heat pumps are appearing as replacements and have their own fault patterns, mostly around the compressor and sensors.</p>
<p>Repair versus replacement, and how the systems stack up, is covered on the general """ + L("hot-water", "hot water page") + """. Tempering valve faults have their own page: """ + L("hot-water-tempering-valves", "tempering valves") + """. A cylinder emptying itself onto a laundry floor is urgent, and the """ + H("hot water emergency page") + """ page lists the steps. We attend """ + L("plumber-eight-mile-plains", "Eight Mile Plains") + """, """ + L("plumber-rochedale-south", "Rochedale South") + """ and """ + L("hot-water-springwood", "Springwood") + """ from Yatala, grouping southside work together. The company's details are on """ + M("www.moyleplumbing.com.au") + """.</p>
"""),
    faqs=[
        ("My electric unit only heats overnight. Is that a fault?",
         "<p>Probably not. Many southside units are on an off-peak tariff that only powers the unit at night. If a big morning demand empties it, the unit is either too small or one element has failed.</p>"),
        ("Can a leaking tank be repaired?",
         "<p>No. A leak from the tank body means the cylinder has corroded through. Leaks from valves and fittings on the outside of the tank can be fixed.</p>"),
        ("How soon can you attend a no-hot-water call on the southside?",
         "<p>We group southside work and give a truthful arrival window. If the unit is leaking as well, it moves up the list.</p>"),
        ("Is it worth repairing a unit over ten years old?",
         "<p>Where the tank is fine and the failed part is cheap, repairing buys time. With corrosion or a history of repairs, the money is better put toward replacement, and we say so.</p>"),
    ],
    related=[
        ("hot-water-systems-brisbane-southside", "New hot water systems southside"),
        ("hot-water", "Hot water overview"),
        ("hot-water-tempering-valves", "Tempering valves"),
        ("hot-water-springwood", "Hot water Springwood"),
        ("plumber-eight-mile-plains", "Plumber Eight Mile Plains"),
        ("plumber-rochedale-south", "Plumber Rochedale South"),
    ],
)
