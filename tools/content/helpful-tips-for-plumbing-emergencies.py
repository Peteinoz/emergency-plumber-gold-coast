from _common import *

page = dict(
    slug="helpful-tips-for-plumbing-emergencies", kind="post", crumb="Emergency tips",
    title="Helpful Tips for Plumbing Emergencies | Moyle Plumbing",
    description='Plumbing emergency tips: find the water meter, shut off gas safely, isolate a leaking hot water unit and limit the damage. Call (07) 3807 7327.',
    h1="Helpful tips for plumbing emergencies",
    eyebrow="Handy hints",
    intro="<p>Helpful tips for plumbing emergencies come down to one idea: you can stop the damage before the plumber arrives, and the sooner you do it, the less there is to fix. This article walks through where the shut-offs are in a typical Gold Coast home, what to do for each kind of emergency, and the mistakes that make things worse.</p>",
    breadcrumb=[("handy-hints-blog", "Handy hints")],
    post=dict(published="2026-09-18", modified="2026-09-18"),
    body=sec("""
<h2>Know your shut-offs before you need them</h2>
<p>Take ten minutes on a calm day to find these four things. In an emergency you will not want to be searching.</p>
<ol class="steps">
<li><strong>The water meter.</strong> In a box near the front boundary, usually close to the driveway or letterbox, sometimes on the footpath. The tap or lever beside the dial turns off clockwise. Try it once so you know it moves; old meter taps can be stiff. In a unit complex, meters are grouped near the entry and each is labelled with a lot number.</li>
<li><strong>The gas meter or cylinders.</strong> Natural gas meters sit on an outside wall with a valve on the inlet pipe; off is when the handle lies across the pipe. LPG cylinders have a hand wheel on top that closes clockwise.</li>
<li><strong>The hot water breaker.</strong> In the switchboard, labelled hot water, HWS or water heater. This is how you make a leaking unit safe.</li>
<li><strong>The fixture isolation valves.</strong> Small taps under basins and sinks, behind toilets and at the washing machine. They let you stop one fixture without turning off the house.</li>
</ol>
""") + soft("""
<h2>What to do for each emergency</h2>
<h3>A pipe or hose has burst</h3>
<p>Meter off, or the valve at the fixture if only one basin or toilet is involved. Open a low tap to drain the pressure. Kill the power to any circuit the water could reach. Move rugs and anything electrical. Photograph the damage. Then ring.</p>
<h3>You can smell gas</h3>
<p>Turn off the gas at the meter or the cylinder. Ventilate. Do not touch light switches, appliances, phones near the smell, or anything that could spark. Get everyone outside. Ring from outside: a licensed gasfitter to find and fix the leak, and the gas network's emergency line if the smell is strong. Never go looking for the leak with a flame or a match, and never try to fix it yourself.</p>
<h3>The hot water unit is leaking</h3>
<p>Breaker off first, then close the cold water tap on the pipe into the unit. Keep away from the heater and the puddle until the power is off. Water from the cylinder itself means the heater is finished; a dribble at the relief valve while it heats can be normal, and we can tell you which on the phone.</p>
<h3>Sewage is coming up</h3>
<p>Stop using water: no flushing, no showers, no washing machine. Check the overflow gully outside; if it is releasing, that is by design. Keep kids and animals clear of anything that has overflowed. Ring us, and keep drain chemicals out of it.</p>
<h3>Water is coming through the ceiling</h3>
<p>Switch off the lighting circuit for that room at the board. Catch the drip in a bucket and, if the plaster is bulging, pierce it carefully with a screwdriver at the lowest point over the bucket to let the water out before it brings the plaster down. Find the source above: a bathroom, a hot water unit in the roof, or the roof itself.</p>
""") + sec("""
<h2>Mistakes that make it worse</h2>
<ul>
<li><strong>Resetting a breaker that keeps tripping.</strong> It is tripping because something is wet or faulty. Leave it off.</li>
<li><strong>Tape and clamps on a burst pipe.</strong> They do not hold mains pressure. Isolate instead.</li>
<li><strong>Chemical drain cleaners.</strong> They rarely clear a real blockage, they attack old pipes, and they put whoever opens the drain next at risk.</li>
<li><strong>Turning the gas back on to see if the smell has gone.</strong> It has not. Wait for the test.</li>
<li><strong>Waiting to see if it stops.</strong> Leaks do not stop; they get into slabs and walls.</li>
</ul>
<h2>What to tell the plumber</h2>
<p>Your suburb, what is happening, what you have turned off, and the hot water and gas setup if it is involved. A photo sent ahead by email means we arrive with the right parts. On genuine emergencies Moyle Plumbing &amp; Gasfitting aims for same-day attendance from Yatala, and the repair carries a fixed figure agreed ahead of any work.</p>
<p>The whole sequence, from call to clean-up, is on the """ + H("emergency plumbing home page for the Gold Coast") + """ home page, with the detail for each problem under """ + L("burst-pipe", "burst pipe repair") + """, """ + L("blocked-drains", "drain clearing") + """, """ + L("hot-water", "hot water faults") + """ and """ + L("gas-fitting", "gas leaks") + """. More general questions are answered in our """ + L("frequently-asked-questions", "frequently asked questions") + """ article. The advice comes from a family business started in 1983; see """ + M("the company's main website") + """.</p>
"""),
    faqs=[
        ("The water meter tap will not turn. What now?",
         "<p>Do not force it with a tool; old taps snap. Use the isolation valves at the fixtures to stop what you can, open a low tap to drop the pressure, and ring us. We carry the tools to shut a stiff meter safely.</p>"),
        ("Should I call the water company or a plumber?",
         "<p>If the leak is before the meter, on the footpath or verge, it belongs to the water utility. Anything after the meter is yours, and a plumber is the call.</p>"),
        ("Is a dripping relief valve on the hot water unit an emergency?",
         "<p>A small discharge while the unit heats is normal. A stream that never stops is a failed valve or excess pressure and should be booked, but it is not urgent unless the unit is also leaking from the tank.</p>"),
        ("Can I keep using the toilet if the sewer is blocked?",
         "<p>No. Every flush adds to the overflow. Stop using water until the line is cleared.</p>"),
    ],
    related=[
        ("emergency-plumbing", "Emergency plumbing"),
        ("burst-pipe", "Burst pipes"),
        ("gas-fitting", "Gas fitting"),
        ("hot-water", "Hot water"),
        ("frequently-asked-questions", "Plumbing FAQs"),
        ("handy-hints-blog", "Handy hints"),
    ],
)
