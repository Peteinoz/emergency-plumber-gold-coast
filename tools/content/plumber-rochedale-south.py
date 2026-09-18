from _common import *

page = dict(
    slug="plumber-rochedale-south", kind="suburb", crumb="Plumber Rochedale South",
    title="Plumber Rochedale South | 1970s–80s Homes | Moyle",
    description="Plumber for Rochedale South's brick-and-tile homes: ageing pipes, original bathrooms, tree roots in drains and hot water replacement. Call (07) 3807 7327.",
    h1="Plumber Rochedale South",
    eyebrow="Rochedale South QLD 4123",
    intro="<p>A plumber in Rochedale South works almost entirely on brick-and-tile homes from the 1970s and 1980s. That makes the suburb predictable in a useful way: the same materials are reaching the same age in every street. Moyle Plumbing &amp; Gasfitting comes up from Yatala for repairs, replacements and renovations, with the price agreed before starting.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Rochedale South", area="Rochedale South"),
    body=sec("""
<h2>What forty-year-old plumbing looks like</h2>
<table>
<thead><tr><th>Component</th><th>Typical condition now</th><th>What we do</th></tr></thead>
<tbody>
<tr><td>Copper water pipes</td><td>Pinholes on hot lines, green staining at joints</td><td>Section replacement or reroute; pressure test</td></tr>
<tr><td>Galvanised water service (oldest streets)</td><td>Rusted internally, low pressure, brown water</td><td>Replace with new pipe from meter to house</td></tr>
<tr><td>Earthenware or early PVC sewer</td><td>Root intrusion at joints, occasional cracks</td><td>Clear, camera, repair sections as needed</td></tr>
<tr><td>Tap bodies and breeches</td><td>Worn seats, stiff spindles</td><td>Reseat and re-washer, or replace with mixers</td></tr>
<tr><td>Toilet suites</td><td>Single flush, seeping outlet washers</td><td>Replace with dual-flush suites</td></tr>
<tr><td>Shower waterproofing</td><td>At or past its life; damp in adjoining rooms</td><td>Test, then repair or renovate</td></tr>
<tr><td>Hot water unit</td><td>Second or third replacement due</td><td>Replace; heat pump often worth it</td></tr>
<tr><td>Gas connectors</td><td>Original flexible connectors perished</td><td>Replace and leak test</td></tr>
</tbody>
</table>
""") + soft("""
<h2>Roots and established gardens</h2>
<p>Rochedale South's gardens have had decades to send roots into the sewer, and root blockages are the most common emergency we attend here. Clearing gets the line open; the camera afterwards tells you whether the pipe is cracked. Where it is, relaying that section breaks the cycle. Where it is sound, an occasional booked clean holds it there. Detail is on the """ + L("blocked-drains", "blocked drains page") + """.</p>
<h2>Original bathrooms</h2>
<p>Many homes still have the first bathroom, and the waterproofing under the tiles has long since given up. Leaks show as damp on the bedroom side of the wall or swollen skirting. We test the recess to separate a plumbing fault from a membrane failure; see """ + L("leaking-shower-repairs", "leaking shower repairs") + """. Where the whole room is coming out, the plumbing side is covered under """ + L("bathroom-renovations", "bathroom renovations") + """, and for owners staying put as they age, """ + L("bathroom-modifications", "bathroom modifications") + """.</p>
""") + sec("""
<h2>Getting to Rochedale South</h2>
<p>We drive up from Yatala and bundle southside jobs into the one trip. For anything that has already failed, shut things off as described on the """ + H("Rochedale South emergency plumber page") + """ and ring """ + PHONE + """. """ + L("plumber-eight-mile-plains", "Eight Mile Plains") + """, Springwood and Underwood are on the same run, and leak work across the suburb is covered under """ + L("leak-repairs", "leak detection") + """. Moyle Plumbing &amp; Gasfitting, family owned from 1983 to today, has its background on """ + M("the Moyle Plumbing website") + """.</p>
""") + sec("""
<h2>Renovating without surprises</h2>
<p>Rochedale South's homes are being renovated in large numbers, and a renovation is when forty-year-old plumbing gets found out. Before a kitchen or bathroom is stripped we recommend a camera through the drains and a pressure test on the water, because discovering a broken sewer or a pinholed copper run after the new tiles are down is the expensive way to learn about it. Where the pipes are at the end of their life, replacing them during the renovation adds a modest amount to the job and saves opening a new wall two years later. We work with your builder on the program and price the plumbing scope in writing.</p>
"""),
    faqs=[
        ("Should I replace all the copper at once or as it fails?",
         "<p>If one pinhole has appeared, more are coming. Replacing the hot lines, which fail first, or rerouting the worst runs is a sensible middle path. We give you the options with set prices.</p>"),
        ("How often should roots be cleared?",
         "<p>It depends on the trees and the pipe. Once we have seen the line on camera we can suggest an interval, often every year or two, that stays ahead of a blockage.</p>"),
        ("Can you replace a 1970s toilet with a modern one?",
         "<p>Yes. We match the new suite to the existing outlet position so the tiles stay where they are.</p>"),
        ("Is it worth a pre-purchase plumbing check on a house this age?",
         "<p>Definitely. Camera footage of the sewer and a pressure test of the pipework can show whether a new drain or a repipe is coming. See our pre-purchase inspection service.</p>"),
    ],
    related=[
        ("blocked-drains", "Blocked drains"),
        ("leaking-shower-repairs", "Leaking showers"),
        ("leak-repairs", "Leak detection"),
        ("hot-water", "Hot water"),
        ("prepurchase-plumbing-inspection", "Pre-purchase inspection"),
        ("plumber-eight-mile-plains", "Plumber Eight Mile Plains"),
        ("hot-water-springwood", "Hot water Springwood"),
    ],
)
