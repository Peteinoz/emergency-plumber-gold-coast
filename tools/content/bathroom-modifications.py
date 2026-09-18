from _common import *

page = dict(
    slug="bathroom-modifications", kind="service", crumb="Bathroom modifications",
    title="Bathroom Modifications Gold Coast | Moyle Plumbing",
    description='Bathroom modifications for accessibility on the northern Gold Coast and Logan: walk-in showers, raised toilets, lever taps. Call (07) 3807 7327.',
    h1="Bathroom modifications for safer, easier use",
    eyebrow="Accessibility",
    intro="<p>Bathroom modifications let people stay in their own home longer, recover from surgery safely or live with a disability without a full renovation. Moyle Plumbing &amp; Gasfitting handles the plumbing side across the northern Gold Coast and Logan: hobless showers, hand-held showers, raised or wall-faced toilets, lever taps and the drainage changes that make each of them work.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Bathroom modifications", area="Gold Coast"),
    body=sec("""
<h2>Common modifications and what they involve</h2>
<table>
<thead><tr><th>Modification</th><th>Plumbing work</th></tr></thead>
<tbody>
<tr><td>Bath removed, walk-in shower installed</td><td>New floor waste position, drainage regrade, shower mixer and rail, waterproofing coordination</td></tr>
<tr><td>Hob removed from an existing shower</td><td>Floor waste relocated or upgraded, screen and waterproofing redone by the relevant trades</td></tr>
<tr><td>Raised-height or wall-faced toilet</td><td>New suite, outlet adaptor, cistern position changed to suit rails</td></tr>
<tr><td>Hand-held shower on a slide rail</td><td>Mixer and outlet changed; rail positioned for seated use</td></tr>
<tr><td>Lever or sensor taps</td><td>Mixer replacement, often with a pressure check</td></tr>
<tr><td>Thermostatic mixing valve</td><td>Fitted at the shower or the hot water unit so water cannot scald</td></tr>
<tr><td>Basin at wheelchair height</td><td>Wall-hung basin, trap relocated for knee clearance</td></tr>
</tbody>
</table>
""") + soft("""
<h2>Working with occupational therapists and funders</h2>
<p>Many modifications come from an occupational therapist's recommendation and are funded through a home care package, the NDIS or an insurer. We work from the therapist's specification, quote the plumbing scope as a set price so the funder has a clear figure, and coordinate with the builder, tiler and waterproofer so the sequence is right. Where a grab rail or shower seat is specified, we make sure the plumbing does not end up where the rail needs to go.</p>
<p>Because scald protection matters more for people with reduced sensation or slower reactions, we check the """ + L("hot-water-tempering-valves", "tempering valve") + """ on every modification job and fit a thermostatic mixer where the therapist asks for one.</p>
""") + sec("""
<h2>Small changes that help straight away</h2>
<ul class="checks">
<li>Replacing twist taps with lever mixers that a stiff hand can operate.</li>
<li>Fitting a hand-held shower to an existing outlet so someone can wash seated.</li>
<li>Swapping a low toilet for a taller suite without moving the drain.</li>
<li>Adjusting the hot water temperature at the tempering valve so the shower cannot be set dangerously hot.</li>
<li>Adding a second shower mixer at a lower height for a carer.</li>
</ul>
<p>Where the whole room is being redone, the """ + L("bathroom-renovations", "bathroom renovation plumbing page") + """ covers the wider job, and a shower that is leaking as well is dealt with under """ + L("leaking-shower-repairs", "leaking shower repairs") + """. New suites are described on the """ + L("toilets", "toilets page") + """. If a modification job uncovers a live leak, we handle it as we would any urgent fault on the """ + H("urgent plumber page") + """ page. We do this work through """ + L("plumber-shailer-park", "Shailer Park") + """, """ + L("plumber-rochedale-south", "Rochedale South") + """ and """ + L("plumber-eight-mile-plains", "Eight Mile Plains") + """ as well as the northern Gold Coast, and the business has been family run since 1983, and its details sit on """ + M("the main Moyle site") + """.</p>
""") + sec("""
<h2>Planning the visit</h2>
<p>Before quoting we ask for the therapist's report if there is one, a photo of the bathroom and a note on who will use it and how. That tells us whether a hand-held shower and a lever mixer will do, or whether the bath has to come out. Most modification quotes are prepared from a single site visit, and where the floor waste has to move we check the drain route with a camera during that visit so the price does not change once tiles are lifted. Materials are chosen for grip, reach and cleaning as much as for looks: lever handles, outlets at seated height and traps tucked back for knee room.</p>
"""),
    faqs=[
        ("Can a bath be turned into a walk-in shower?",
         "<p>Yes, and it is the most requested modification. The bath is removed, the floor waste is repositioned and the floor graded to it, then the area is waterproofed and tiled. We handle the plumbing and coordinate with the other trades.</p>"),
        ("Do you work with NDIS or aged care funding?",
         "<p>We provide set-price quotes from the occupational therapist's specification in the format funders ask for, and complete the plumbing scope as specified.</p>"),
        ("Will I be without a bathroom during the work?",
         "<p>For a shower conversion the room is out of action for several days while waterproofing cures and tiling is done. We sequence our work to keep the toilet usable wherever possible and tell you the timeline before starting.</p>"),
    ],
    related=[
        ("bathroom-renovations", "Bathroom renovation plumbing"),
        ("leaking-shower-repairs", "Leaking shower repairs"),
        ("toilets", "Toilet replacement"),
        ("hot-water-tempering-valves", "Tempering valves"),
        ("plumber-shailer-park", "Plumber Shailer Park"),
        ("plumber-rochedale-south", "Plumber Rochedale South"),
        ("plumber-eight-mile-plains", "Plumber Eight Mile Plains"),
    ],
)
