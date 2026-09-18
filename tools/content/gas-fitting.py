from _common import *

page = dict(
    slug="gas-fitting", kind="service", crumb="Gas fitting",
    title="Licensed Gas Fitter Gold Coast | Moyle Plumbing & Gasfitting",
    description='Licensed gas fitter for the northern Gold Coast, Beenleigh and Logan. Gas leaks, appliances, hot water and cooktops, certified. Call (07) 3807 7327.',
    h1="Licensed gas fitter, Gold Coast",
    eyebrow="Gas fitting",
    intro="<p>A licensed gas fitter is the only person who should touch a gas line in Queensland, and Moyle Plumbing &amp; Gasfitting has held that licence alongside its plumbing licence for decades. From Yatala we handle gas leaks, new appliance connections, hot water, cooktops, heaters and bottled gas installations across the northern Gold Coast.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Gas fitting", area="Gold Coast"),
    body=sec("""
<h2>If you smell gas</h2>
""" + callout("""<ol>
<li>Shut the gas at the meter (natural gas) or the cylinder valve (LPG). It is off when the handle is at right angles to the pipe.</li>
<li>Ventilate the house. Do not operate light switches, appliances or anything that could spark. Do not smoke or light anything.</li>
<li>Get everyone outside and make the call from there: ring us on """ + PHONE + """ and, if the smell is strong, your gas network's emergency line too.</li>
<li>Do not try to find or fix the leak yourself, and do not turn the gas back on until it has been tested.</li>
</ol>""", warn=True) + """
<p>A slight smell only when an appliance lights, a pilot that will not stay lit or a yellow lazy flame on a cooktop are also signs something needs attention, even if they are not an emergency yet.</p>
""") + soft("""
<h2>Gas work we do</h2>
""" + cards([
    ("hot-water", "Gas hot water", "Storage and continuous flow units supplied, installed, converted from electric and repaired, including gas line upgrades where the supply is undersized."),
    ("bbq-gas-bottle", "BBQ and outdoor gas", "Bayonet points for barbecues and patio heaters, and proper LPG bottle installations for homes without mains gas."),
    ("commercial-plumbing", "Commercial gas", "Kitchens, cafes and workshops: appliance connections, isolation valves and installation tests."),
    ("emergency-plumbing", "Leak detection and repair", "Pressure testing the installation, locating the leak and repairing it, then testing again before gas is restored."),
]) + """
<p>Also cooktops and ovens, ducted and flued heaters, gas line extensions for renovations, and the disconnection of old appliances when a kitchen is replaced.</p>
""") + sec("""
<h2>What a proper gas job includes</h2>
<ul class="checks">
<li>A check that the existing pipe can supply every appliance at once, not just the new one.</li>
<li>Correct pipe sizing and jointing for the pressure and gas type.</li>
<li>Isolation valves where they are required so one appliance can be shut off without the rest.</li>
<li>Flueing and ventilation checked for any appliance that produces combustion gases indoors.</li>
<li>A pressure and leak test of the whole installation before it is commissioned.</li>
<li>The compliance paperwork that the law requires and that your insurer or a buyer's inspector will ask for.</li>
</ul>
<h2>LPG versus natural gas</h2>
<p>Parts of the northern Gold Coast have reticulated natural gas and many streets do not. Where there is no mains supply, appliances run on LPG from exchange cylinders or a bulk tank. The appliances are different, the regulators are different and the pipe sizing is different, so tell us which you have when you ring. If you are moving into a house and are unsure, we can check.</p>
<p>Our gas work reaches """ + L("plumber-pimpama", "Pimpama") + """, """ + L("plumber-helensvale", "Helensvale") + """, """ + L("plumber-ormeau", "Ormeau") + """, Coomera and Hope Island, plus Beenleigh, Logan and Brisbane's southside. A gas leak is its own kind of emergency, and the """ + H("gas leak emergency page") + """ covers it in the first-steps list. The company's details are on the """ + M("Moyle Plumbing &amp; Gasfitting") + """ main website.</p>
""") + sec("""
<h2>Buying or renting a home with gas</h2>
<p>If you are moving into a house with gas appliances, ask for the compliance paperwork for the installation and the date the appliances were last serviced. If nobody can find either, a gas safety check is a sensible first step: we leak test the pipework, check each appliance's flame and flue, confirm the isolation valves work and give you a written result. Landlords in particular should have this on file, because a tenant reporting a gas smell becomes a very different conversation when the installation has a recent test behind it. The check is quick, priced as a fixed figure, and can be combined with a plumbing inspection of the same property.</p>
"""),
    faqs=[
        ("Can a plumber legally work on gas?",
         "<p>Only if they hold a gas work licence, which is separate from a plumbing licence. Moyle Plumbing &amp; Gasfitting holds both, so the same tradesperson can do the water and gas sides of a hot water or kitchen job.</p>"),
        ("Do I get a certificate after gas work?",
         "<p>Yes. Licensed gas work in Queensland comes with compliance documentation that records the installation and the test. Keep it with your house papers.</p>"),
        ("How can I tell if my cooktop flame is safe?",
         "<p>A healthy flame is blue with a steady shape. Yellow, orange, sooty or lifting flames mean incomplete combustion and the appliance should be checked before further use.</p>"),
        ("Can you convert my electric hot water to gas?",
         "<p>Often, yes, if the property has a gas supply or can take an LPG installation and there is a suitable location for the flue. We check the supply, the location and the drainage of the relief line before quoting.</p>"),
    ],
    related=[
        ("bbq-gas-bottle", "BBQ gas connections"),
        ("hot-water", "Hot water systems"),
        ("emergency-plumbing", "Emergency plumbing"),
        ("commercial-plumbing", "Commercial plumbing"),
        ("plumber-pimpama", "Plumber Pimpama"),
        ("plumber-helensvale", "Plumber Helensvale"),
        ("plumber-ormeau", "Plumber Ormeau"),
    ],
)
