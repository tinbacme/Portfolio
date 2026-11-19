// ATS-friendly resume (Word), built from the "Tin Le — Resume 2026" doc (the master copy).
// Rules followed, from ATS formatting research: one column; no tables, text boxes, images, headers or footers;
// contact info in the body with text labels; standard headings; each role's title, employer and dates on one line
// (dates set with a right tab stop); real Word bullets; one standard font (Calibri). **bold** in the text below = bold run.
// usage: node make-docx.js  -> Tin-Le-Resume.docx
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, TabStopType, BorderStyle, LevelFormat, HeadingLevel, AlignmentType } = require('docx');
const FONT = 'Calibri', INK = '000000', MUT = '3c3c3c';
const W = 12240, M = 900, RIGHT = W - 2 * M, SZ = 19;

const runs = (text, o = {}) => text.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((t) => {
  const b = t.startsWith('**');
  return new TextRun({ text: b ? t.slice(2, -2) : t, font: FONT, size: o.size || SZ, bold: b || !!o.bold, color: o.color || (b ? INK : MUT) });
});
const para = (text, o = {}) => new Paragraph({ spacing: { after: o.after ?? 40 }, children: runs(text, o) });
const heading = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t.toUpperCase(), font: FONT, size: 21, bold: true, color: INK })] });
const line = (left, right, o = {}) => new Paragraph({ spacing: { before: o.before ?? 100, after: 10 }, keepNext: true, tabStops: [{ type: TabStopType.RIGHT, position: RIGHT }],
  children: [...runs(left, { color: INK }), new TextRun({ text: '\t' + right, font: FONT, size: SZ, color: INK })] });
const sub = (t) => new Paragraph({ spacing: { after: 20 }, keepNext: true, children: runs(t, { size: 19, color: '555555' }) });
const bullet = (t) => new Paragraph({ numbering: { reference: 'dots', level: 0 }, spacing: { after: 12 }, children: runs(t) });

const doc = new Document({
  creator: 'Tin Le', title: 'Tin Le Resume',
  styles: {
    default: { document: { run: { font: FONT, size: SZ } } },
    paragraphStyles: [{ id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
      run: { font: FONT, size: 21, bold: true, color: INK },
      paragraph: { spacing: { before: 150, after: 40 }, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '999999', space: 2 } } } }],
  },
  numbering: { config: [{ reference: 'dots', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 340, hanging: 220 } } } }] }] },
  sections: [{ properties: { page: { size: { width: W, height: 15840 }, margin: { top: 640, bottom: 560, left: M, right: M } } }, children: [
    new Paragraph({ spacing: { after: 30 }, children: [new TextRun({ text: 'Tin Le', font: FONT, size: 38, bold: true, color: INK })] }),
    para('**Senior Product Designer | Search & AI Experiences** · Portland, OR', { size: 21, after: 30 }),
    para('LinkedIn: linkedin.com/in/letin08', { size: 19, after: 60 }),
    para('Senior product designer with 9 years shipping consumer and enterprise products. At Microsoft AI I design search and AI experiences across Bing, Edge and Windows, after five years at Salesforce on Help, partner and design-system work. I also teach UX/UI design at the University of Oregon.'),

    heading('Experience'),
    line('**Senior Designer**, Microsoft AI', 'May 2022 – Present', { before: 60 }),
    sub('Portland · Designer II (2022) → Senior Designer (Present)'),
    bullet('**Bing growth campaigns:** Design growth campaigns across Bing, Edge and Windows, from holidays and cultural moments to the FIFA World Cup 2026, which reached **1.71M impressions** and drove ~**120% app installs** during that month.'),
    bullet('**Copilot and AI agents:** Led vision work for an Agentic Bing and prototyped agent task flows end to end, testing three prototypes with **14 participants** to pick a direction; also designed the **notification system for the Copilot app** and Copilot answers in Windows search (2025–26).'),
    bullet('**Windows and Edge search:** Redesigned the Bing results inside the Windows search box and tested it through 10 rounds of A/B preference tests and moderated user research studies and manage an external agency; led Windows sprints on the calendar and a lock screen widget and new Windows 11 Search Experience for release.'),
    bullet('**Bing Real Estate:** Designed and shipped Bing\'s rental marketplace end to end, plus its design system. Saved homes, map clustering and owner claim flows drove **+15% daily active users**, **103K homes saved** and **25K properties claimed**.'),
    bullet('**Design leadership:** Build AI design tools for teams, including an AI image gens, Figma plugin, internal design tools, and teach **prototyping with AI** in Microsoft AI\'s internal AI academy program. Grew ProtoPie licenses from **3 to 23** after a workshop for **64 designers**; manage one direct report.'),

    line('**Salesforce**', 'Jun 2017 – May 2022'),
    sub('Portland, OR'),
    line('**Designer**', '2020 – May 2022', { before: 30 }),
    bullet('**Salesforce Help site redesign:** Led research and design for the first major update since 2012. After launch, support cases dropped 60% month over month.'),
    bullet('**Partner portal user management:** Shipped an MVP in 2 weeks that cut related support cases 32% month over month, then led the full redesign to a 6.2/7 usability score. One of 8+ features I designed for Salesforce\'s partner portal.'),
    bullet('Designed a back-to-work app that helped **75K employees** return to offices safely during COVID-19, and contributed components to **Salesforce\'s C360 and SLDS 2 design systems**, working with 12 product teams.'),
    line('**Associate Designer**', '2018 – 2020', { before: 50 }),
    bullet('Worked with stakeholders to map customer experiences, find pain points and spot opportunities, then designed wireframe concepts with the Salesforce Lightning Design System.'),
    bullet('Created a standard research-to-handoff template for the design team, cutting prep time by **80%**.'),
    line('**UX Design Intern**', '2017', { before: 50 }),
    bullet('Redesigned onboarding for new employees with a portal to find information, search for benefits and manage their profiles.'),

    heading('Teaching'),
    line('**Instructor**, University of Oregon', '2023 – Present', { before: 60 }),
    bullet('Teach UX/UI Design (PD 410, PD 460) each year: research, case studies, prototyping, and midterm and final critiques.'),
    line('**UX/UI Instructor**, 2U bootcamps', 'Feb 2021 – [end date]'),
    bullet('Led cohorts through a 24-week UX/UI certificate (research, UX and UI design, front-end basics) for six university programs: Utah, Oregon, UC Berkeley, Michigan, Minnesota and Arizona.'),

    heading('Skills'),
    para('**Design:** product and interaction design, visual design, design systems, high-fidelity prototyping, usability testing and A/B concept testing, design sprints and workshops, accessibility reviews', { after: 20 }),
    para('**Industrial design:** sketching, 3D modeling, rendering, physical prototyping', { after: 20 }),
    para('**Tools:** Figma (including plugin development), ProtoPie, Adobe Creative Suite, Blender, Rhino, KeyShot, After Effects, Webflow, HTML/CSS/JS, AI prototyping tools, Claude Code, Codex, Github, AI toolings', { after: 20 }),

    heading('Education'),
    para('**University of Oregon** — BS, Product Design, Minor in Business Administration'),

    heading('Awards'),
    para('2nd place overall — KIVA Hackathon, 2021 · 3rd place overall — Salesforce Hackathon, 2020'),
  ] }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(__dirname + '/Tin-Le-Resume.docx', b); console.log('ok', b.length); });
