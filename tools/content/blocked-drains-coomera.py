from _common import *

page = dict(
    slug="blocked-drains-coomera", kind="suburb", crumb="Blocked drains Coomera",
    title="Blocked Drains Coomera | Cleared & Inspected | Moyle",
    description="Blocked drains in Coomera cleared by Yatala-based plumbers with jetting, cable machines and camera inspection. Sewer and stormwater. Call (07) 3807 7327.",
    h1="Blocked drains Coomera",
    eyebrow="Drains only",
    intro="<p>Blocked drains in Coomera have their own patterns. The suburb's PVC drains rarely fail from age, but construction debris, tree roots on the older blocks and the sheer volume of wipes going down new estates' sewers keep us busy. Moyle Plumbing &amp; Gasfitting comes from Yatala with the jetter, the cable machine and the camera, and prices the job before starting.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Blocked drain clearing in Coomera", area="Coomera"),
    body=sec("""
<h2>Which drain is it?</h2>
<ul class="checks">
<li><strong>Kitchen sink only:</strong> grease in the kitchen line. Jetting clears it properly; a cable just pokes a hole through it.</li>
<li><strong>Shower or bath slow, toilet fine:</strong> hair and soap in the bathroom branch.</li>
<li><strong>Toilet gurgles, floor waste bubbles, water at the gully outside:</strong> the main sewer. Stop all water use and ring """ + PHONE + """.</li>
<li><strong>Yard flooding or a downpipe overflowing in rain:</strong> stormwater, which on Coomera estates often means silt or building rubble.</li>
</ul>
""") + soft("""
<h2>Why Coomera drains block</h2>
<table>
<thead><tr><th>Cause</th><th>Where we see it</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Wipes and sanitary items</td><td>Every estate, every week</td><td>Cable machine, then a talk about the bin</td></tr>
<tr><td>Grease</td><td>Kitchen lines in busy family homes</td><td>High-pressure jetting</td></tr>
<tr><td>Construction rubble in stormwater</td><td>Newer stages of estates</td><td>Jetting and camera, occasional pit clean-out</td></tr>
<tr><td>Tree roots</td><td>Older blocks along the original roads and river flats</td><td>Root cutting, camera, repair if the pipe is cracked</td></tr>
<tr><td>Sagging pipe from ground settlement</td><td>Filled sites on the flats</td><td>Camera to locate, excavate and relay the section</td></tr>
<tr><td>Poorly glued joints from construction</td><td>Any new home</td><td>Locate with camera, dig and rejoint</td></tr>
</tbody>
</table>
""") + sec("""
<h2>How the job runs</h2>
<ol class="steps">
<li>We find the inspection openings and the overflow gully and work out which line is affected.</li>
<li>The clearing cost is named before any machine leaves the van.</li>
<li>The line is cleared with the right tool for the cause, then run with water to confirm it is flowing.</li>
<li>If the drain has blocked before, or the cause is not obvious, a camera goes through and you see the footage.</li>
<li>Any repair the camera reveals is priced separately and is your call.</li>
</ol>
<p>Drains are just one of the jobs we do around Coomera; the """ + L("plumber-coomera", "Coomera plumber page") + """ covers the rest. The general approach and prevention advice sit on the main """ + L("blocked-drains", "blocked drains page") + """, and if the blockage has sewage coming up inside, treat it as urgent and use the """ + H("Coomera emergency plumber page") + """ page. Ormeau has similar issues with a rural twist: see """ + L("blocked-drains-ormeau", "blocked drains Ormeau") + """. Overflowing toilets are covered under """ + L("toilets", "toilets") + """. The company's details are on """ + M("moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>Coomera stormwater in a summer storm</h2>
<p>The flat parts of Coomera drain slowly at the best of times, and a summer downpour shows up every weak point: downpipes discharging onto the ground instead of into a pit, pits half full of silt from the last stage of construction, and charged lines that have been crushed by a delivery truck across the verge. If your yard or garage floods before the street does, the line between roof and kerb is the place to look. We jet the stormwater, camera it and, where a section is crushed, dig and relay it, usually in a day. It is worth doing before the wet season rather than after.</p>
"""),
    faqs=[
        ("Is the drain still under builder warranty?",
         "<p>Possibly, if the home is new and the blockage is from a construction defect such as rubble or a bad joint. Our camera footage and report give you what you need to make the claim.</p>"),
        ("Why does the drain block again a few months after clearing?",
         "<p>Because the cause was not removed. Roots regrow, grease rebuilds and a sagging pipe keeps collecting. A camera inspection after clearing shows whether a repair is needed to stop the cycle.</p>"),
        ("Do you clear stormwater as well as sewer?",
         "<p>Yes. Stormwater lines, pits and downpipe connections are cleared with the jetter, which is the right tool for silt and rubble.</p>"),
        ("What should I do while waiting for you?",
         "<p>Stop using water so nothing more goes down the line, keep people away from any overflow, and if it is sewage, hose the area down once we have cleared it.</p>"),
    ],
    related=[
        ("blocked-drains", "Blocked drains overview"),
        ("plumber-coomera", "Plumber Coomera"),
        ("blocked-drains-ormeau", "Blocked drains Ormeau"),
        ("toilets", "Toilet repairs"),
        ("plumber-pimpama", "Plumber Pimpama"),
        ("plumber-hope-island", "Plumber Hope Island"),
    ],
)
