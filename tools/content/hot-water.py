from _common import *

page = dict(
    slug="hot-water", kind="service", crumb="Hot water",
    title="Hot Water System Repairs & Replacement | Moyle Plumbing",
    description='Hot water system repairs and replacement across the northern Gold Coast, Logan and Brisbane southside. All fuel types. Call (07) 3807 7327.',
    h1="Hot water system repairs and replacement",
    eyebrow="Hot water",
    intro="<p>Losing hot water is one of those faults that turns a normal morning into a bad one. Moyle Plumbing &amp; Gasfitting repairs and replaces electric, gas, solar and heat pump hot water systems from its Yatala base, and because the business is licensed for both plumbing and gas, one tradesperson can handle the whole job.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Hot water system repair and replacement", area="Gold Coast"),
    body=sec("""
<h2>Quick checks before you call</h2>
<p>Two minutes here can save a visit, or tell us exactly what to bring.</p>
<ol class="steps">
<li><strong>Electric storage:</strong> look at the switchboard. If the hot water breaker has tripped, reset it once. If it trips again, leave it off: the element or thermostat has most likely failed and the circuit is doing its job.</li>
<li><strong>Gas storage:</strong> check whether the pilot is lit and whether other gas appliances are working. If the cooktop is also out, the supply is the problem, not the heater.</li>
<li><strong>Continuous flow gas:</strong> is the unit showing an error code? Note it down. Check the power point the unit plugs into and the gas isolation tap under it.</li>
<li><strong>Any type:</strong> is water running from the base of the cylinder, or just a trickle from the relief valve on the side? A leaking cylinder needs replacing; a dribbling relief valve during heating is often normal, but a constant stream is not.</li>
</ol>
""" + callout("<p><strong>If the cylinder is leaking:</strong> switch the unit off at the switchboard before anything else, then close the cold water isolation tap on the inlet pipe. Do not touch the unit or the water with the power still on.</p>", warn=True) + """
""") + soft("""
<h2>Repair or replace?</h2>
<p>We will always tell you which one we would choose in your position. The rough rules:</p>
<table>
<thead><tr><th>Fault</th><th>Usual answer</th></tr></thead>
<tbody>
<tr><td>Failed element or thermostat, tank sound</td><td>Repair</td></tr>
<tr><td>Relief valve running constantly</td><td>Repair (valve replacement)</td></tr>
<tr><td>Tempering valve failed, water too hot or cold</td><td>Repair (see """ + L("hot-water-tempering-valves", "tempering valves") + """)</td></tr>
<tr><td>Cylinder rusted through or leaking from the tank</td><td>Replace</td></tr>
<tr><td>Older unit with a second major fault</td><td>Usually replace</td></tr>
<tr><td>Continuous flow unit with error code</td><td>Diagnose first; often repairable</td></tr>
</tbody>
</table>
<p>Either way you get a set price before we start, and if you choose replacement we take the old unit away.</p>
""") + sec("""
<h2>Choosing a new hot water system</h2>
<p>The right unit depends on the existing setup, the number of people and the running costs you can live with.</p>
<ul>
<li><strong>Electric storage:</strong> the simplest swap where one already exists. Cheapest to buy, dearest to run unless on an off-peak tariff.</li>
<li><strong>Gas storage or continuous flow:</strong> good recovery and lower running cost if the home already has gas. Continuous flow never runs out but needs adequate gas supply and, for some models, a power point.</li>
<li><strong>Heat pump:</strong> draws far less electricity than a plain electric tank and thrives in this climate. Needs airflow around it and can be heard running.</li>
<li><strong>Solar:</strong> lowest running cost with a boosted tank, but the biggest upfront job and it needs suitable roof space.</li>
</ul>
<p>Government rebates and energy retailer schemes change often, so ask us what applies at the time. In Queensland the installation must also have a tempering valve feeding the bathrooms and come from a licensed plumber, with the gas side handled by a licensed gasfitter. We hold both licences.</p>
<h2>Local hot water pages</h2>
<p>There are separate pages for """ + L("hot-water-gold-coast", "hot water on the Gold Coast") + """, """ + L("hot-water-system-logan", "hot water systems in Logan") + """, """ + L("hot-water-springwood", "Springwood") + """, and both """ + L("hot-water-repairs-brisbane-southside", "repairs") + """ and """ + L("hot-water-systems-brisbane-southside", "new systems") + """ on Brisbane's southside, because the housing and the existing installations differ from area to area.</p>
<p>A heater dripping through a ceiling or flooding a laundry is urgent. The """ + H("no hot water emergency page") + """ home page lists what to isolate first. Company background and history sit on the """ + M("Moyle Plumbing website") + """.</p>
"""),
    faqs=[
        ("What is the lifespan of a hot water system?",
         "<p>Water quality, unit type and whether the anode was ever changed all matter. Many storage tanks see ten years or more, and serviced continuous flow units frequently outlast them. If yours is leaking from the tank body, it is at the end regardless of age.</p>"),
        ("Can you replace it the same day?",
         "<p>Frequently, if it is a straight swap of a common storage size. If the unit is unusual, or you want to change fuel type or location, it may take a second visit. We will tell you when you call.</p>"),
        ("Why is my hot water lukewarm rather than off?",
         "<p>On a twin-element electric tank, one element has usually failed. Whatever the system, a tired tempering valve or a mixer tap cross-connecting hot and cold can do the same. All are repairable.</p>"),
        ("Is water dripping from the valve on the side normal?",
         "<p>A small discharge from the pressure and temperature relief valve while the tank heats is normal. A steady stream, or discharge all day, means the valve has failed or the pressure is too high and it should be looked at.</p>"),
    ],
    related=[
        ("hot-water-tempering-valves", "Tempering valves"),
        ("hot-water-gold-coast", "Hot water Gold Coast"),
        ("hot-water-system-logan", "Hot water Logan"),
        ("hot-water-repairs-brisbane-southside", "Repairs Brisbane southside"),
        ("hot-water-systems-brisbane-southside", "New systems Brisbane southside"),
        ("hot-water-springwood", "Hot water Springwood"),
        ("gas-fitting", "Gas fitting"),
    ],
)
