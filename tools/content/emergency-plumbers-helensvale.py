from _common import *

page = dict(
    slug="emergency-plumbers-helensvale", kind="suburb", crumb="Emergency plumbers Helensvale",
    title="Emergency Plumbers Helensvale | Urgent Callouts | Moyle",
    description='Emergency plumbers for Helensvale: burst pipes, no hot water, blocked sewers and gas leaks attended from Yatala, priced first. Call (07) 3807 7327.',
    h1="Emergency plumbers Helensvale",
    eyebrow="Urgent callouts only",
    intro="""<p>Emergency plumbers for Helensvale need to be close and need to be honest about timing. Moyle Plumbing &amp; Gasfitting is at Yatala, up the M1, and when the situation is urgent we plan to be there that day. This page is for the faults that cannot wait; for everyday work in the suburb see the """ + L("plumber-helensvale", "Helensvale plumber page") + """.</p>""",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Emergency plumbing in Helensvale", area="Helensvale"),
    body=sec("""
<h2>Is it urgent? A quick triage</h2>
<table>
<thead><tr><th>What you see</th><th>Do this now</th><th>Then</th></tr></thead>
<tbody>
<tr><td>Water pouring from a hose, pipe or tap that will not close</td><td>Meter off (clockwise until it stops)</td><td>Ring us</td></tr>
<tr><td>Sewage at the outside gully, shower or toilet</td><td>Stop using all water</td><td>Ring us</td></tr>
<tr><td>Gas smell</td><td>Meter or cylinder off, windows open, no switches, get outside</td><td>Ring us from outside</td></tr>
<tr><td>Hot water cylinder leaking from the tank body</td><td>Switch off at the switchboard, then close its cold inlet tap</td><td>Ring us</td></tr>
<tr><td>Water arriving through a ceiling or light fitting</td><td>Switch off that lighting circuit, meter off if it keeps coming</td><td>Ring us</td></tr>
<tr><td>Dripping tap, slow basin, cistern trickling</td><td>Nothing urgent</td><td>Book a visit</td></tr>
</tbody>
</table>
""") + soft("""
<h2>Why Helensvale gets these calls</h2>
<p>The suburb's housing is mostly thirty to forty years old. That age brings a predictable set of emergencies:</p>
<ul>
<li><strong>Hot water tanks rusting through</strong>, often discovered as a flooded laundry or garage in the morning.</li>
<li><strong>Copper pinholes</strong> in walls and beneath slabs, noticed as a warm floor or a damp carpet edge.</li>
<li><strong>Sewer blockages from roots</strong> in gardens that have had decades to grow.</li>
<li><strong>Flexible hoses from 2000s renovations</strong> bursting under the kitchen sink or vanity.</li>
<li><strong>Stormwater overwhelmed</strong> around the canals during a summer storm, backing up into garages and yards.</li>
</ul>
""") + sec("""
<h2>What the callout looks like</h2>
<ol class="steps">
<li>You ring """ + PHONE + """ and say what is wrong and which valves are already closed.</li>
<li>We give you a realistic arrival window from Yatala. Helensvale is a direct run south on the highway.</li>
<li>The plumber isolates the fault, works out the proper repair and names the price before starting.</li>
<li>The repair is done and tested, and the area is cleaned up. If the fault points to something bigger, such as a failing hot water unit or a drain that needs relaying, you get that advice in writing to decide on later.</li>
</ol>
<p>The main """ + H("Gold Coast emergency plumbing repairs") + """ page explains the whole process and the safety rules for gas, water and electricity. Related detail is under """ + L("burst-pipe", "burst pipes") + """, """ + L("blocked-drains", "blocked drains") + """ and """ + L("hot-water", "hot water") + """. Nearby """ + L("plumber-hope-island", "Hope Island") + """ and """ + L("plumber-coomera", "Coomera") + """ are attended from the same base. The business behind this service is described on """ + M("our main website") + """.</p>
""") + sec("""
<h2>Insurance and paperwork</h2>
<p>Water damage claims are common in Helensvale's older homes, and insurers ask the same things every time: what failed, when, whether it was sudden, and what was done to stop it. Photograph everything before you start mopping, keep the failed part if we replace it, and ask us for the invoice description to be specific about the cause. Most policies cover the resulting damage from a sudden failure and not the worn part itself, so the cause description matters. If an assessor wants to speak to the plumber who attended, that is fine; the number is on every page of this site.</p>
"""),
    faqs=[
        ("Can you come to Helensvale today?",
         "<p>For a genuine emergency that is the aim, and you will hear at once whether the day allows it. No promises we cannot meet.</p>"),
        ("What if I cannot find my water meter?",
         "<p>Look in a small box near the front boundary, often near the driveway or letterbox. In a townhouse complex, meters are usually banked together near the entry. If you cannot find it, close the isolation valve at the fixture and ring us; we will talk you through it.</p>"),
        ("Do you carry hot water units for same-day replacement?",
         "<p>Common electric and gas storage sizes, yes. If your unit is unusual we will tell you on the phone and get the right one in.</p>"),
        ("Is a strong gas smell something you handle or the gas company?",
         "<p>Both. Isolate the gas, get outside, ring the gas network's emergency number if the smell is strong, and ring us to find and repair the leak and test the installation.</p>"),
    ],
    related=[
        ("plumber-helensvale", "Plumber Helensvale"),
        ("emergency-plumbing", "Emergency plumbing"),
        ("burst-pipe", "Burst pipes"),
        ("blocked-drains", "Blocked drains"),
        ("hot-water", "Hot water"),
        ("plumber-hope-island", "Plumber Hope Island"),
        ("plumber-coomera", "Plumber Coomera"),
    ],
)
