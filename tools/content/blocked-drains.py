from _common import *

page = dict(
    slug="blocked-drains", kind="service", crumb="Blocked drains",
    title="Blocked Drain Plumber Gold Coast | Moyle Plumbing",
    description='Blocked drain plumber for the northern Gold Coast, Beenleigh and Logan. Jetting, cable machines and camera inspection, priced first. Call (07) 3807 7327.',
    h1="Blocked drain plumber, Gold Coast",
    eyebrow="Drains and sewer",
    intro="<p>A blocked drain plumber does more than poke a cable down the pipe. From Yatala, Moyle Plumbing &amp; Gasfitting clears kitchen, bathroom, stormwater and sewer blockages across the northern Gold Coast, finds out why they happened, and gives you the price before the machine comes off the van.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Blocked drain clearing", area="Gold Coast"),
    body=sec("""
<h2>How to tell which drain is blocked</h2>
<p>Where the water backs up tells you a lot, and it changes how urgent the job is.</p>
<ul>
<li><strong>One fixture slow, the rest fine:</strong> the blockage is in that fixture's trap or branch. Hair and soap in a shower, fat and food in a kitchen sink. Annoying, not urgent.</li>
<li><strong>Toilet gurgles when the shower drains, or water rises in the floor waste:</strong> the branch that serves the bathroom group is restricted. Book it soon.</li>
<li><strong>Everything slow, water rising at the overflow gully outside:</strong> the main sewer is blocked. That gully is doing its job by releasing outside rather than inside the house, but stop using water and ring us.</li>
<li><strong>Puddles in the yard or a downpipe spilling over in rain:</strong> stormwater, usually roots or silt, sometimes a crushed pipe.</li>
</ul>
<p>If sewage is coming up inside the house, treat it as an emergency and call """ + PHONE + """. We cover it under """ + L("emergency-plumbing", "emergency plumbing") + """.</p>
""") + soft("""
<h2>Why drains block on the northern Gold Coast</h2>
<p>Across Coomera, Pimpama, Ormeau and the older streets of Beenleigh we see the same handful of causes over and over:</p>
<ul class="checks">
<li><strong>Tree roots.</strong> Roots find the joints in older earthenware and even in poorly glued PVC. Once inside, they act as a net for everything that follows.</li>
<li><strong>Fat, oil and grease.</strong> Poured down a kitchen sink warm, it sets further down the line and narrows the pipe a little more every week.</li>
<li><strong>Wipes and sanitary products.</strong> "Flushable" wipes do not break down. They tangle on any rough edge and build a plug.</li>
<li><strong>Sagging or broken pipe.</strong> Ground movement, heavy vehicles over the line or a builder's excavator nicking the pipe. A camera finds it; a cable machine only clears it for a while.</li>
<li><strong>New-build debris.</strong> On newer estates we sometimes find render, grout or concrete washed into stormwater drains during construction.</li>
</ul>
""") + sec("""
<h2>What we bring and how we clear it</h2>
<p>Different blockages need different tools, and using the wrong one can damage the pipe.</p>
<ul>
<li><strong>Drain cable machine:</strong> the standard tool for cutting through roots and breaking up soft blockages in sewer lines.</li>
<li><strong>High-pressure water jetter:</strong> scours grease and silt off the pipe wall and flushes it away, which a cable cannot do. The right choice for kitchen lines and stormwater.</li>
<li><strong>Drain camera:</strong> a small camera run through the line after clearing to show what caused it and whether the pipe is damaged. You see the footage.</li>
<li><strong>Locator:</strong> pinpoints where a broken section sits underground so any dig is small and in the right place.</li>
</ul>
<p>Once the plumber has seen the access points and the layout, clearing is priced as a single job. If the camera finds a broken or collapsed section, the repair is quoted separately and you decide whether to proceed.</p>
<h2>Keeping it clear afterwards</h2>
<p>Once the line is open, a few habits stop the next call:</p>
<ul>
<li>Fat into a jar or the bin, never the sink, even with hot water behind it.</li>
<li>Only toilet paper down the toilet. Wipes go in the bin regardless of what the packet says.</li>
<li>A strainer in the shower waste and the kitchen sink.</li>
<li>Where roots are the cause, a maintenance clean every year or two is far cheaper than digging.</li>
</ul>
<p>Our local area pages for """ + L("blocked-drains-coomera", "blocked drains in Coomera") + """ and """ + L("blocked-drains-ormeau", "blocked drains in Ormeau") + """ go into the specific pipe types and estate layouts in those suburbs. When a sewer problem has become urgent, the """ + H("emergency drain and plumbing page") + """ page covers what to do before we get there.</p>
<p>The business behind this site, """ + M("Moyle Plumbing &amp; Gasfitting") + """, has cleared drains around Yatala and the northern Gold Coast since 1983.</p>
"""),
    faqs=[
        ("Can I clear a blocked drain myself first?",
         "<p>For a single slow basin or shower, a plunger or removing and cleaning the trap is fine. Avoid caustic drain chemicals: they rarely shift a real blockage, they damage older pipes, and they make the job dangerous for whoever opens the drain next.</p>"),
        ("Do you use a camera on every job?",
         "<p>Not always. If a kitchen line is simply full of grease, jetting clears it and a camera adds nothing. Where a sewer keeps blocking, roots are suspected or a pipe may be broken, the camera is worth it and we will tell you before running it.</p>"),
        ("Is the overflow gully outside supposed to leak?",
         "<p>Yes, that is its purpose. When the sewer backs up, the gully releases outside so sewage does not surface inside the house. If it is overflowing, the main line is blocked and needs clearing.</p>"),
        ("Who is responsible for a blockage in a rental property?",
         "<p>Generally the owner is responsible for the drains, but a tenant can be charged where wipes, fat or similar misuse caused it. Agencies send us plenty of this work, and we note the cause once the line is clear.</p>"),
    ],
    related=[
        ("blocked-drains-coomera", "Blocked drains Coomera"),
        ("blocked-drains-ormeau", "Blocked drains Ormeau"),
        ("toilets", "Toilet repairs"),
        ("leak-repairs", "Leak detection"),
        ("emergency-plumbing", "Emergency plumbing"),
        ("plumber-helensvale", "Plumber Helensvale"),
        ("plumber-loganholme", "Plumber Loganholme"),
    ],
)
