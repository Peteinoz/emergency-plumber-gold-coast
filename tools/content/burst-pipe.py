from _common import *

page = dict(
    slug="burst-pipe", kind="service", crumb="Burst pipes",
    title="Burst Pipe Repair Gold Coast | Moyle Plumbing & Gasfitting",
    description='Burst pipe repair across the northern Gold Coast, Beenleigh and Logan. Isolate, locate, repair and pressure test, price set first. Call (07) 3807 7327.',
    h1="Burst pipe repair, northern Gold Coast",
    eyebrow="Burst and split pipes",
    intro="<p>Burst pipe repair starts with you, not the plumber: the faster the water is off, the smaller the damage. This page tells you how to isolate it, what a burst looks like when it is hidden, and how Moyle Plumbing &amp; Gasfitting finds and fixes the failed section from its base at Yatala.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Burst pipe repair", area="Gold Coast"),
    body=sec("""
<h2>Right now: stop the water</h2>
<ol class="steps">
<li><strong>Find the water meter.</strong> Usually in a plastic or concrete box near the front boundary, sometimes on the footpath. Turn the tap clockwise until it stops. On a unit or townhouse there may be an isolation valve for your lot near the meter bank or in the garage.</li>
<li><strong>If the burst is at one fixture,</strong> use the small isolation valve under the basin, behind the toilet or at the washing machine taps so the remainder of the house stays supplied.</li>
<li><strong>Open a tap</strong> at the lowest point to drain pressure out of the pipes and slow the leak.</li>
<li><strong>Cut the power</strong> to any circuit close to the water, and to the hot water unit if the burst is on its pipework.</li>
<li>Then ring """ + PHONE + """.</li>
</ol>
""") + soft("""
<h2>Where pipes burst around here, and why</h2>
<ul>
<li><strong>Flexible hoses under sinks and vanities.</strong> The braided hose behind a mixer tap is the most common cause of a flooded house on the Gold Coast. They fail without warning, often at night, and they flow at full mains pressure.</li>
<li><strong>Copper under slabs and in walls.</strong> Beenleigh, Loganholme and Springwood have older copper that can pit or corrode from the inside, or rub through where it passes a joist. Electrolysis can also eat copper from within.</li>
<li><strong>Poly pipe in the yard.</strong> Blue-line poly between the meter and the house cracks at fittings, gets nicked by garden tools or fails at a joint that was never crimped properly.</li>
<li><strong>Water hammer and high pressure.</strong> Mains pressure in some newer estates is high enough to stress every joint in the house. A limiting valve on the incoming supply is cheap insurance.</li>
<li><strong>Hot water pipework.</strong> The connections on top of a storage tank corrode and split, especially where two different metals meet.</li>
</ul>
""") + sec("""
<h2>Finding a burst you cannot see</h2>
<p>A burst under the slab or inside a wall shows up as a warm patch on the floor, a wet skirting, a meter that keeps turning with every tap off, or a water bill that has jumped. We use pressure testing to confirm which pipe has failed, then acoustic and thermal equipment to locate it before opening anything. That is a separate service in its own right: see """ + L("leak-repairs", "leak detection and repair") + """.</p>
<h2>The repair</h2>
<p>Once located, the failed section is cut out and replaced with new pipe and proper fittings, not a clamp or tape. The line is pressure tested before the wall, floor or trench is closed. Where a pipe has failed because of poor pressure or electrolysis, we deal with the cause as well so the next section along does not go the same way. You get the figure before the repair begins, and anything a wall reveals is discussed before it is dealt with.</p>
<p>A burst is the plainest case of the urgent work set out on the """ + H("Gold Coast emergency plumber") + """ page, and it is covered under our general """ + L("emergency-plumbing", "emergency plumbing") + """ service. Routine pipework and tap work is under """ + L("general-plumbing-maintenance", "plumbing maintenance") + """. The trading history of """ + M("Moyle Plumbing") + """ goes back to 1983.</p>
"""),
    faqs=[
        ("My water meter is spinning with everything off. Is that a burst?",
         "<p>Almost certainly a leak somewhere between the meter and your taps. Turn the meter off to stop the loss and ring us. We pressure test to isolate which section is leaking and locate it before digging.</p>"),
        ("Can I patch the pipe with tape until you arrive?",
         "<p>Tape and clamps rarely hold at mains pressure. Isolating the water at the meter is the reliable stopgap. If you must have water on, use the fixture isolation valves so only the damaged section is off.</p>"),
        ("Will the repair be covered by insurance?",
         "<p>Many home policies cover resulting water damage but not the worn part that failed. Photograph everything before clean-up and keep our invoice, which describes the cause.</p>"),
        ("Why do flexible hoses keep failing?",
         "<p>The braided sheath corrodes, the rubber inner ages and the crimped ends work loose. Replacing them every several years and fitting quality hoses with isolation taps is far cheaper than a flooded kitchen.</p>"),
    ],
    related=[
        ("leak-repairs", "Leak detection"),
        ("emergency-plumbing", "Emergency plumbing"),
        ("hot-water", "Hot water systems"),
        ("general-plumbing-maintenance", "Plumbing maintenance"),
        ("emergency-plumber-beenleigh", "Emergency plumber Beenleigh"),
        ("emergency-plumbers-helensvale", "Emergency plumbers Helensvale"),
        ("plumber-pimpama", "Plumber Pimpama"),
    ],
)
