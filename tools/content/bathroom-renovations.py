from _common import *

page = dict(
    slug="bathroom-renovations", kind="service", crumb="Bathroom renovations",
    title="Bathroom Renovation Plumbing Gold Coast | Moyle Plumbing",
    description='Bathroom renovation plumbing on the northern Gold Coast and Logan: rough-in, drainage changes, fit-off and certification. Call (07) 3807 7327.',
    h1="Bathroom renovation plumbing",
    eyebrow="Renovations",
    intro="<p>Bathroom renovation plumbing is the part of the job you never see once the tiles are on, which is exactly why it has to be right. Moyle Plumbing &amp; Gasfitting does the rough-in, drainage changes, hot water upgrades and final fit-off for bathroom renovations across the northern Gold Coast and Logan, working with your builder or directly with you.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Bathroom renovation plumbing", area="Gold Coast"),
    body=sec("""
<h2>The plumbing stages of a renovation</h2>
<ol class="steps">
<li><strong>Planning.</strong> We look at where the existing drains and pipes run, tell you what can move cheaply and what cannot, and check the hot water system will cope with a bigger shower or a second bathroom.</li>
<li><strong>Strip-out.</strong> Fixtures are disconnected and capped so the demolition can go ahead with the water on to the rest of the house.</li>
<li><strong>Rough-in.</strong> New water lines, drainage and floor wastes are installed to suit the layout, and pressure tested. This is when the toilet outlet, shower waste and vanity connections are set.</li>
<li><strong>Waterproofing and tiling</strong> by the relevant trades, with our puddle flanges and wall penetrations in place first.</li>
<li><strong>Fit-off.</strong> Mixers, toilet suite, basin, bath, shower rose and rails fitted, connected and tested.</li>
<li><strong>Certification.</strong> Plumbing and drainage work is documented as required, so the renovation is compliant when you sell.</li>
</ol>
""") + soft("""
<h2>What changes cost and what they save</h2>
<table>
<thead><tr><th>Change</th><th>Plumbing impact</th></tr></thead>
<tbody>
<tr><td>Keeping fixtures in the same positions</td><td>Least work; usually fit-off only with new tapware</td></tr>
<tr><td>Moving the toilet</td><td>Drain relocation, often a slab cut on ground floors</td></tr>
<tr><td>Bath to walk-in shower</td><td>New floor waste and regrade; see """ + L("bathroom-modifications", "bathroom modifications") + """</td></tr>
<tr><td>Wall-hung toilet or basin</td><td>In-wall cistern frame and concealed pipework before the wall is sheeted</td></tr>
<tr><td>Freestanding bath</td><td>Floor-mounted spout and a waste in the right spot before the slab or floor is closed</td></tr>
<tr><td>Rain shower plus hand shower</td><td>Diverter mixer and two outlets, with a check of pressure and hot water capacity</td></tr>
</tbody>
</table>
<p>Set pricing applies to renovations as it does to repairs: the plumbing scope is priced in writing before work begins, and changes you ask for during the job are priced before they are done.</p>
""") + sec("""
<h2>Getting the hot water right</h2>
<p>A new bathroom with a larger shower head, a deep bath or a second ensuite can outrun an old hot water unit. We check capacity during planning and, where an upgrade makes sense, fold it into the job. Every renovated bathroom in Queensland also needs tempered water at the shower and basin, so the """ + L("hot-water-tempering-valves", "tempering valve") + """ is checked or fitted at the same time. See the """ + L("hot-water", "hot water page") + """ for options.</p>
<h2>Working with your builder</h2>
<p>We are used to slotting into a builder's program: rough-in on the day the frame is ready, back for fit-off when the tiler is done, and a phone call rather than a delay if something on site does not match the plan. If you are managing the renovation yourself, we tell you which trade needs to be in when.</p>
<p>Renovations also uncover old problems. A shower that was quietly leaking for years is found when the tiles come off; the """ + L("leaking-shower-repairs", "leaking shower page") + """ explains what to look for. A new suite is chosen with the help of the """ + L("toilets", "toilets page") + """. And if something lets go mid-renovation with water running, the """ + H("urgent repairs page") + """ has the isolation steps. Renovation work takes us to """ + L("plumber-hope-island", "Hope Island") + """, """ + L("plumber-coomera", "Coomera") + """ and """ + L("plumber-shailer-park", "Shailer Park") + """ regularly. Company history is on the """ + M("Moyle Plumbing &amp; Gasfitting") + """ main site.</p>
"""),
    faqs=[
        ("Can we move the toilet to the other wall?",
         "<p>Usually yes, but on a slab it means cutting the concrete to run a new drain, which adds cost and time. On a timber floor it is simpler. We tell you the difference before you commit to a layout.</p>"),
        ("Do you supply the tapware and fixtures?",
         "<p>Either. Many clients choose their own from a showroom and we install it; we can also supply from brands we know hold up. Whichever way, we check compatibility with your water pressure and the hot water system.</p>"),
        ("How long is the plumbing part of a renovation?",
         "<p>Rough-in is typically a day or two, and fit-off another day, spread across the builder's program. The waterproofing and tiling between them are what set the overall length.</p>"),
        ("Is a plumbing certificate needed for the renovation?",
         "<p>In Queensland, new drainage and water work is licensed work and is documented as the rules require. Keep the paperwork with the house records for when you sell.</p>"),
    ],
    related=[
        ("bathroom-modifications", "Bathroom modifications"),
        ("leaking-shower-repairs", "Leaking shower repairs"),
        ("toilets", "Toilets"),
        ("hot-water", "Hot water systems"),
        ("plumber-hope-island", "Plumber Hope Island"),
        ("plumber-coomera", "Plumber Coomera"),
        ("plumber-shailer-park", "Plumber Shailer Park"),
    ],
)
