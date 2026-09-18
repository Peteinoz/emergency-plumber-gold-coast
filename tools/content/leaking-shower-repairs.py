from _common import *

page = dict(
    slug="leaking-shower-repairs", kind="service", crumb="Leaking showers",
    title="Leaking Shower Repairs Gold Coast | Moyle Plumbing",
    description='Leaking shower repairs on the northern Gold Coast and Logan. We find whether it is the tap, the waste or the waterproofing. Call (07) 3807 7327.',
    h1="Leaking shower repairs",
    eyebrow="Wet areas",
    intro="<p>Leaking shower repairs start with one question: is the water coming from the plumbing or from the recess itself? The answer decides whether you need a plumber, a waterproofer or both. Moyle Plumbing &amp; Gasfitting tests showers across the northern Gold Coast to find out, and fixes the plumbing side with the price agreed first.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Leaking shower repairs", area="Gold Coast"),
    body=sec("""
<h2>Where shower leaks come from</h2>
<ul>
<li><strong>The mixer or tap body inside the wall.</strong> Water appears behind the wall or in the room next door, whether or not the shower is running, if a pressure pipe is involved. A dripping tap that runs into the recess is the easy version.</li>
<li><strong>The shower rose arm and its wall connection.</strong> Water tracks back along the arm into the wall cavity every time the shower runs.</li>
<li><strong>The floor waste and its puddle flange.</strong> If the waste was not sealed to the waterproofing, water gets under the tiles and out through the slab or subfloor.</li>
<li><strong>The waterproof membrane.</strong> Failed at the hob, the wall-floor junction or the screen fixings. Water leaks only when the shower is used, and shows up as damp carpet, swollen skirting or a stain on the ceiling below.</li>
<li><strong>The screen and grout.</strong> Water escaping onto the bathroom floor, not into the structure. Annoying rather than damaging, as long as the floor is waterproofed.</li>
</ul>
""") + soft("""
<h2>How we test it</h2>
<ol class="steps">
<li><strong>Pressure test</strong> both supply lines to the shower with the taps shut. Loss means a pipe or tap body leak.</li>
<li><strong>Flood test</strong> the recess by plugging the waste and filling the floor to just below the hob, then watching for water at the adjoining room, the ceiling below or the meter. Loss means waterproofing or the waste seal.</li>
<li><strong>Run the shower</strong> onto the walls only, then the floor only, to separate wall leaks from floor leaks.</li>
<li><strong>Moisture meter and thermal camera</strong> on the walls and floor around the recess to map where water has been going.</li>
</ol>
<p>You get a clear answer: plumbing fault, waterproofing fault or both, and a set price for the plumbing repair. Where the membrane has failed we tell you honestly that regrouting or a surface seal is a short-term fix and that the recess needs to be redone.</p>
""") + sec("""
<h2>The plumbing repairs</h2>
<ul class="checks">
<li>Mixer body or breech replaced, with the wall opened from the back where possible to save tiles.</li>
<li>Shower arm resealed and refitted; wall elbow replaced where corroded.</li>
<li>Floor waste and puddle flange replaced and integrated with new waterproofing.</li>
<li>Drainage checked with a camera if the waste has been slow, since a partly blocked shower line can be the reason the recess floods over the hob.</li>
</ul>
<p>If the leak is running into a downstairs light fitting or through a ceiling, turn the shower off, turn the meter off and follow the """ + H("leak emergency page") + """ before ringing. For leaks elsewhere in the house the process is described under """ + L("leak-repairs", "leak detection and repair") + """. Where the recess needs rebuilding, that becomes a """ + L("bathroom-renovations", "bathroom renovation") + """ or, for a hobless conversion, a """ + L("bathroom-modifications", "bathroom modification") + """. A cracked toilet nearby is often blamed for a shower leak; the """ + L("toilets", "toilets page") + """ explains how to tell. We do this work across """ + L("plumber-helensvale", "Helensvale") + """ and """ + L("plumber-loganholme", "Loganholme") + """ and the suburbs between, and you can read more about """ + M("our full plumbing website") + """.</p>
"""),
    faqs=[
        ("Can a leaking shower be fixed without retiling?",
         "<p>If the leak is a tap body, shower arm or waste seal, yes, usually with a small opening that a tiler can patch. If the membrane itself has failed, a surface sealant may buy a little time but the proper fix is to strip and waterproof the recess again.</p>"),
        ("Why is the wall on the other side of my shower damp?",
         "<p>Either the tap body or pipe inside that wall is leaking under pressure, or water is getting through the wall tiles and membrane when the shower runs. A pressure test tells us which within minutes.</p>"),
        ("Is a leaking shower covered by insurance?",
         "<p>Policies differ. Sudden pipe failures are often covered; slow leaks from failed waterproofing frequently are not. Our written diagnosis helps you make the claim either way.</p>"),
        ("Should I stop using the shower?",
         "<p>If water is reaching another room or a ceiling, yes, until it is tested. If it is only escaping onto the bathroom floor, it can usually wait for a booked visit.</p>"),
    ],
    related=[
        ("leak-repairs", "Leak detection"),
        ("bathroom-renovations", "Bathroom renovations"),
        ("bathroom-modifications", "Bathroom modifications"),
        ("toilets", "Toilet repairs"),
        ("plumber-helensvale", "Plumber Helensvale"),
        ("plumber-loganholme", "Plumber Loganholme"),
    ],
)
