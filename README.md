# Awesome Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo-light.svg" width="120" alt="Awesome Lists logo: a stack of three cards with a star on the front one">
  </picture>
</p>

An awesome list is a hand-picked collection of the best tools, libraries and reading on one topic, kept in a public repo that anyone can improve. There are thousands of them, which creates its own problem: you have to know the right list exists before it can help you.

This is a list of lists. It points to one good starting place for each topic, from Kubernetes and Rust to accessibility and testing, so you can find the right one in a minute instead of an afternoon.

To use it, browse the sections below or search the page (Ctrl+F, or Cmd+F on a Mac) for a technology you care about. Each entry gives the list, the person or team behind it and a line on what is inside. There are 675 lists so far.

## Contents

- [DevOps](#devops)
  - [Automation and scripting](#automation-and-scripting)
  - [CI/CD](#cicd)
  - [General and SRE](#general-and-sre)
  - [Infrastructure as code](#infrastructure-as-code)
  - [Kubernetes and containers](#kubernetes-and-containers)
  - [Observability](#observability)
- [Cloud](#cloud)
  - [AWS](#aws)
  - [Azure](#azure)
  - [Cloudflare](#cloudflare)
  - [Free tiers and discounts](#free-tiers-and-discounts)
  - [Other providers and PaaS](#other-providers-and-paas)
  - [Serverless](#serverless)
- [Shift left](#shift-left)
  - [DevSecOps and secure SDLC](#devsecops-and-secure-sdlc)
  - [Pipeline security](#pipeline-security)
  - [Policy as code](#policy-as-code)
  - [Pre-commit and Git hooks](#pre-commit-and-git-hooks)
  - [Static and dynamic analysis](#static-and-dynamic-analysis)
  - [Supply chain security](#supply-chain-security)
- [Architecture](#architecture)
  - [Microservices and scale](#microservices-and-scale)
  - [Software architecture](#software-architecture)
  - [System design](#system-design)
- [Developer tools](#developer-tools)
  - [Chat platforms](#chat-platforms)
  - [Chrome and browsers](#chrome-and-browsers)
  - [CLI and terminal](#cli-and-terminal)
  - [Editors](#editors)
  - [Git and GitHub](#git-and-github)
  - [Linux desktop](#linux-desktop)
  - [No-code and low-code](#no-code-and-low-code)
  - [Notes and knowledge](#notes-and-knowledge)
  - [Platforms](#platforms)
- [Self-hosting](#self-hosting)
- [Programming languages](#programming-languages)
  - [Across languages](#across-languages)
  - [Ada](#ada)
  - [C and C++](#c-and-c)
  - [C#](#c)
  - [Clojure](#clojure)
  - [Common Lisp](#common-lisp)
  - [Crystal](#crystal)
  - [D](#d)
  - [Dart and Flutter](#dart-and-flutter)
  - [Elixir](#elixir)
  - [Elm](#elm)
  - [F#](#f)
  - [Fortran](#fortran)
  - [Gleam](#gleam)
  - [Go](#go)
  - [Haskell](#haskell)
  - [Java](#java)
  - [JavaScript and TypeScript](#javascript-and-typescript)
  - [Kotlin](#kotlin)
  - [Mojo](#mojo)
  - [Nim](#nim)
  - [OCaml](#ocaml)
  - [Odin](#odin)
  - [Pascal and Delphi](#pascal-and-delphi)
  - [PHP](#php)
  - [Prolog](#prolog)
  - [Python](#python)
  - [R](#r)
  - [Roc](#roc)
  - [Rocq and proof assistants](#rocq-and-proof-assistants)
  - [Ruby](#ruby)
  - [Rust](#rust)
  - [Scala](#scala)
  - [Scheme](#scheme)
  - [Shell](#shell)
  - [Swift](#swift)
  - [V](#v)
  - [VBA](#vba)
  - [Zig](#zig)
- [Web development](#web-development)
  - [Backend and servers](#backend-and-servers)
  - [CSS and graphics](#css-and-graphics)
  - [Frameworks and libraries](#frameworks-and-libraries)
  - [Mobile and cross-platform](#mobile-and-cross-platform)
  - [Performance and the platform](#performance-and-the-platform)
  - [Static sites](#static-sites)
- [APIs](#apis)
- [Data](#data)
  - [Data analysis](#data-analysis)
  - [Data engineering](#data-engineering)
  - [Databases](#databases)
  - [Geospatial](#geospatial)
  - [Open data](#open-data)
- [Security](#security)
  - [AI security](#ai-security)
  - [Cloud security](#cloud-security)
  - [Cryptography](#cryptography)
  - [Defence and detection](#defence-and-detection)
  - [Hardware and IoT security](#hardware-and-iot-security)
  - [Offensive security](#offensive-security)
  - [Privacy and identity](#privacy-and-identity)
  - [Reverse engineering](#reverse-engineering)
  - [Tools and references](#tools-and-references)
  - [Web and application security](#web-and-application-security)
- [Testing and quality](#testing-and-quality)
- [Accessibility](#accessibility)
- [Design and UX](#design-and-ux)
- [AI and machine learning](#ai-and-machine-learning)
  - [AI coding tools](#ai-coding-tools)
  - [AI safety and governance](#ai-safety-and-governance)
  - [Large language models and agents](#large-language-models-and-agents)
  - [Machine learning and data science](#machine-learning-and-data-science)
  - [Research and models](#research-and-models)
- [Documentation and technical writing](#documentation-and-technical-writing)
- [Hardware and embedded](#hardware-and-embedded)
  - [Boards and microcontrollers](#boards-and-microcontrollers)
  - [Devices and gadgets](#devices-and-gadgets)
  - [Electronics and chips](#electronics-and-chips)
  - [IoT, networks and radio](#iot-networks-and-radio)
  - [Performance and HPC](#performance-and-hpc)
  - [Robotics](#robotics)
- [Games](#games)
  - [Engines and frameworks](#engines-and-frameworks)
  - [Game development](#game-development)
  - [Open source games](#open-source-games)
  - [Retro and fantasy consoles](#retro-and-fantasy-consoles)
- [Media and creative](#media-and-creative)
  - [Audio and video](#audio-and-video)
  - [Graphics and 3D](#graphics-and-3d)
  - [Music](#music)
- [Science and research](#science-and-research)
- [Decentralised web](#decentralised-web)
- [Business and careers](#business-and-careers)
  - [Finance and trading](#finance-and-trading)
  - [Jobs and remote work](#jobs-and-remote-work)
  - [Leadership and management](#leadership-and-management)
  - [Open source and community](#open-source-and-community)
  - [Startups and indie](#startups-and-indie)
- [General](#general)
  - [Everyday apps and sites](#everyday-apps-and-sites)
  - [Inclusion and wellbeing](#inclusion-and-wellbeing)
  - [Indexes of lists](#indexes-of-lists)
  - [Learning](#learning)
  - [Practice and conventions](#practice-and-conventions)
  - [Reading, watching and listening](#reading-watching-and-listening)
  - [Schools and education](#schools-and-education)
- [What qualifies](#what-qualifies)
- [How it stays fresh](#how-it-stays-fresh)

## DevOps

### Automation and scripting

- [awesome-home-assistant](https://github.com/frenck/awesome-home-assistant) by Franck Nijhof - Integrations, add-ons and guides for Home Assistant.
- [awesome-jmeter](https://github.com/aliesbelik/awesome-jmeter) by Aliaksandr Belik - Guides and plugins for JMeter load tests.
- [awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) by Enes Cingöz - Importable n8n workflow templates.
- [awesome-network-automation](https://github.com/networktocode/awesome-network-automation) by Network to Code - Tools, data formats and APIs for automating network devices.
- [awesome-pipeline](https://github.com/pditommaso/awesome-pipeline) by Paolo Di Tommaso - Pipeline and workflow toolkits for data and compute jobs.
- [awesome-workflow-engines](https://github.com/meirwah/awesome-workflow-engines) by Meir Wahnon - Open source workflow engines and orchestrators.

### CI/CD

- [awesome-ci](https://github.com/ligurio/awesome-ci) by Sergey Bronnikov - Continuous integration services and tools, from hosted CI to self-hosted runners.
- [awesome-ciandcd](https://github.com/cicdops/awesome-ciandcd) by cicdops - Tools, services and practices for continuous integration and delivery.
- [awesome-feature-flag-management](https://github.com/andrewdmaclean/awesome-feature-flag-management) by Andrew MacLean - Feature flag tools, services and practices.
- [awesome-runners](https://github.com/jonico/awesome-runners) by Johannes Nicolai - Options for running your own GitHub Actions runners.

### General and SRE

- [awesome-ai-sre](https://github.com/agamm/awesome-ai-sre) by Agam More - AI tools for incident response, on-call and root cause analysis.
- [awesome-backstage](https://github.com/shano/awesome-backstage) by Shane Dowling - Plugins, guides and talks for the Backstage developer portal.
- [awesome-chaos-engineering](https://github.com/adriannovegil/awesome-chaos-engineering) by Adrian Novegil - Chaos engineering tools, principles and articles.
- [awesome-devops](https://github.com/wmariuss/awesome-devops) by Marius Stanca - DevOps platforms, tools and practices gathered in one place.
- [awesome-platform-engineering-tools](https://github.com/seifrajhi/awesome-platform-engineering-tools) by saifeddine Rajhi - Tools, reference architectures and reading for building internal developer platforms.
- [awesome-sre](https://github.com/dastergon/awesome-sre) by Pavlos Ratis - Reading, tools and talks on site reliability and production engineering.
- [awesome-sre-tools](https://github.com/SquadcastHub/awesome-sre-tools) by Squadcast Inc - Tools for incident response, monitoring and on-call work.
- [awesome-sysadmin](https://github.com/awesome-foss/awesome-sysadmin) by awesome-foss - Open source software for people who run servers and networks.
- [howtheysre](https://github.com/upgundecha/howtheysre) by Unmesh Gundecha - How companies run site reliability engineering, from their own blogs and talks.
- [post-mortems](https://github.com/danluu/post-mortems) by Dan Luu - Public post-mortems from real outages, handy for learning how systems fail.

### Infrastructure as code

- [awesome-ansible](https://github.com/ansible-community/awesome-ansible) by Community managed Ansible repositories - Roles, tools and learning material for Ansible.
- [AWESOME-Azure-Bicep](https://github.com/ElYusubov/AWESOME-Azure-Bicep) by Elkhan Yusubov - Blogs, videos, tools and samples for Azure Bicep.
- [awesome-nix](https://github.com/nix-community/awesome-nix) by Nix community projects - Nix and NixOS tools, guides and community projects.
- [awesome-opentofu](https://github.com/virtualroot/awesome-opentofu) by Alejandro Lazaro - Projects and learning material around OpenTofu.
- [awesome-pulumi](https://github.com/pulumiverse/awesome-pulumi) by Pulumiverse - Pulumi examples, providers and articles.
- [awesome-tf](https://github.com/shuaibiyy/awesome-tf) by Shuaib Yunus - Terraform and OpenTofu modules, tools and tutorials.

### Kubernetes and containers

- [awesome-argo](https://github.com/akuity/awesome-argo) by Akuity - Projects and write-ups around Argo CD, Workflows and friends.
- [awesome-cloud-native](https://github.com/rootsongjc/awesome-cloud-native) by Jimmy Song - Cloud native projects, books and learning resources.
- [awesome-compose](https://github.com/docker/awesome-compose) by Docker - Ready-to-run Docker Compose samples for common stacks.
- [awesome-docker](https://github.com/veggiemonk/awesome-docker) by Julien Bisconti - Docker tools, images and learning resources.
- [awesome-gitops](https://github.com/weaveworks/awesome-gitops) by Weaveworks - GitOps tools and reading.
- [awesome-helm](https://github.com/cdwv/awesome-helm) by CodeWave - Helm charts and resources.
- [awesome-k8s-resources](https://github.com/tomhuang12/awesome-k8s-resources) by Tom Huang - Kubernetes tools grouped by job, from cluster provisioning to cost and security.
- [awesome-kubectl-plugins](https://github.com/ishantanu/awesome-kubectl-plugins) by Shantanu Deshpande - A catalogue of kubectl plugins.
- [awesome-kubernetes](https://github.com/ramitsurana/awesome-kubernetes) by Ramit Surana - The wide-ranging list of Kubernetes tools and reading.
- [awesome-kubestronaut](https://github.com/yetmike/awesome-kubestronaut) by Mykhailo - Study material for the CNCF Kubernetes certifications, exam by exam.
- [awesome-kustomize](https://github.com/DevOpsHiveHQ/awesome-kustomize) by DevOps Hive - Tools and guides for Kustomize.
- [awesome-nomad](https://github.com/jippi/awesome-nomad) by Christian Winther - User interfaces, plugins, job files and tutorials for HashiCorp Nomad.
- [awesome-swarm](https://github.com/BretFisher/awesome-swarm) by Bret Fisher - Tools, docs and training for Docker Swarm mode.

### Observability

- [awesome-ebpf](https://github.com/qmonnet/awesome-ebpf) by Quentin Monnet - Projects and reading about eBPF.
- [awesome-observability](https://github.com/adriannovegil/awesome-observability) by Adrian Novegil - Observability tools, practices and reading.
- [awesome-opentelemetry](https://github.com/magsther/awesome-opentelemetry) by Magsther - OpenTelemetry resources and tooling.
- [awesome-prometheus-alerts](https://github.com/samber/awesome-prometheus-alerts) by Samuel Berthe - A collection of ready-made Prometheus alerting rules.
- [awesome-status-pages](https://github.com/ivbeg/awesome-status-pages) by Ivan Begtin - Open source and hosted status page tools, plus public examples.

## Cloud

### AWS

- [awesome-aws-security](https://github.com/jassics/awesome-aws-security) by Sanjeev Jaiswal - Links, books and tutorials for securing AWS.
- [awesome-dynamodb](https://github.com/alexdebrie/awesome-dynamodb) by Alex DeBrie - Books, talks and tools for modelling and running DynamoDB.
- [awesome-eventbridge](https://github.com/boyney123/awesome-eventbridge) by David Boyne - Patterns, talks and example projects for Amazon EventBridge.

### Azure

- [awesome-azure-architecture](https://github.com/lukemurraynz/awesome-azure-architecture) by Luke Murray - Azure architecture guidance, patterns and reference material.
- [awesome-entra](https://github.com/merill/awesome-entra) by Merill Fernando - Tools, learning hubs and shortcuts for Microsoft Entra identity.

### Cloudflare

- [awesome-cloudflare](https://github.com/irazasyed/awesome-cloudflare) by Irfaq Syed - Workers recipes, open source projects and tools for Cloudflare.
- [awesome-cloudflare-selfhosted](https://github.com/theoephraim/awesome-cloudflare-selfhosted) by Theo Ephraim - Open source apps you can run on your own Cloudflare account in place of SaaS.

### Free tiers and discounts

- [awesome-open-source-supporters](https://github.com/zachflower/awesome-open-source-supporters) by Zachary Flower - Companies that give their services free to open source projects.
- [discount-for-student-dev](https://github.com/AchoArnold/discount-for-student-dev) by Acho Arnold - Discounts on software and cloud services for students.
- [free-for-dev](https://github.com/ripienaar/free-for-dev) by R.I.Pienaar - SaaS, PaaS and IaaS offerings with free tiers for developers.
- [free-for-life](https://github.com/wdhdev/free-for-life) by William Harrison - Services with a permanent free plan, from databases and DNS to design tools.

### Other providers and PaaS

- [awesome-hcloud](https://github.com/hetznercloud/awesome-hcloud) by Hetzner Cloud - Libraries, tools and integrations for Hetzner Cloud.
- [awesome-paas](https://github.com/debarshibasak/awesome-paas) by Debarshi Basak - Hosted and self-hosted platforms as a service, cloud IDEs and developer platforms.

### Serverless

- [awesome-serverless](https://github.com/anaibol/awesome-serverless) by Anibal - Serverless frameworks, tools and resources across providers.

## Shift left

### DevSecOps and secure SDLC

- [awesome-security-hardening](https://github.com/decalage2/awesome-security-hardening) by Philippe Lagadec - Hardening guides and tools for operating systems, networks and apps.
- [DevSecOps](https://github.com/sottlmarek/DevSecOps) by Marek Šottl - A large library on building security into delivery pipelines.
- [DevSecOps](https://github.com/hahwul/DevSecOps) by hahwul - A collection and roadmap for people learning DevSecOps.

### Pipeline security

- [awesome-cicd-attacks](https://github.com/TupleType/awesome-cicd-attacks) by Asi Greenholts - Research and write-ups on attacking and defending CI/CD systems.
- [awesome-cicd-security](https://github.com/myugan/awesome-cicd-security) by Muhammad Yuga N. - Ways to keep CI/CD pipelines and their secrets safe.

### Policy as code

- [awesome-compliance](https://github.com/theopenlane/awesome-compliance) by Openlane - Frameworks, tools and libraries for security compliance work.
- [awesome-opa](https://github.com/open-policy-agent/awesome-opa) by Open Policy Agent - Tools, frameworks and articles for Open Policy Agent.
- [awesome-security-GRC](https://github.com/GRC-Engineer/awesome-security-GRC) by Ayoub Fandi - Governance, risk, compliance and audit resources for security teams.

### Pre-commit and Git hooks

- [awesome-git-hooks](https://github.com/CompSciLauren/awesome-git-hooks) by Lauren Vu - Git hooks that catch problems before a commit lands.
- [awesome-git-hooks](https://github.com/aitemr/awesome-git-hooks) by Islam Temirbek - More Git hooks and tools for managing them.

### Static and dynamic analysis

- [awesome-codeql](https://github.com/advanced-security/awesome-codeql) by GitHub Advanced Security - Queries, tools and guides for CodeQL code scanning.
- [dynamic-analysis](https://github.com/analysis-tools-dev/dynamic-analysis) by Analysis Tools - Dynamic analysis tools and linters for many languages.
- [static-analysis](https://github.com/analysis-tools-dev/static-analysis) by Analysis Tools - Static analysis tools and linters for many languages.

### Supply chain security

- [awesome-sbom](https://github.com/awesomeSBOM/awesome-sbom) by awesomeSBOM - Tools and standards for software bills of materials.
- [awesome-software-supply-chain-security](https://github.com/bureado/awesome-software-supply-chain-security) by José Miguel Parrella - Resources on securing how software is built, signed and shipped.
- [npm-security-best-practices](https://github.com/lirantal/npm-security-best-practices) by Liran Tal - Practical settings that make npm, pnpm and Bun installs safer.

## Architecture

### Microservices and scale

- [awesome-microservices](https://github.com/mfornos/awesome-microservices) by Marc Fornós - Principles and technologies for building microservice systems.
- [awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) by Binh Nguyen - Patterns and write-ups on building large, reliable systems.

### Software architecture

- [awesome-ddd](https://github.com/heynickc/awesome-ddd) by Nick Chamberlain - Domain-driven design, CQRS and event sourcing resources.
- [awesome-event-driven-architecture](https://github.com/lutzh/awesome-event-driven-architecture) by Lutz Hühnken - Reading and tools for event-driven systems.
- [awesome-integration](https://github.com/stn1slv/awesome-integration) by Stanislav Deviatov - System integration platforms, message brokers and API gateways.
- [awesome-software-architecture](https://github.com/mehdihadeli/awesome-software-architecture) by Mehdi Hadeli - Articles, videos and other resources for learning software architecture.
- [awesome-software-architecture](https://github.com/simonaronsson/awesome-software-architecture) by Simon Aronsson - Another good collection on software architecture.
- [awesome-wardley-maps](https://github.com/wardley-maps-community/awesome-wardley-maps) by Wardley Maps Community - Reading, courses, tools and real examples of Wardley mapping.

### System design

- [awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) by Ashish Pratap Singh - Free articles and videos on system design concepts, grouped by topic.
- [system-design-primer](https://github.com/donnemartin/system-design-primer) by Donne Martin - A guided path through designing large systems, with worked examples and Anki cards.

## Developer tools

### Chat platforms

- [awesome-slack](https://github.com/matiassingers/awesome-slack) by Matias Singers - Libraries, themes and communities for Slack.
- [awesome-telegram](https://github.com/ebertti/awesome-telegram) by Ezequiel Bertti - Bots, bot libraries, groups and channels for Telegram.

### Chrome and browsers

- [awesome-chrome-devtools](https://github.com/ChromeDevTools/awesome-chrome-devtools) by ChromeDevTools - Tooling and resources for Chrome DevTools.
- [awesome-userscripts](https://github.com/awesome-scripts/awesome-userscripts) by awesome-scripts - Userscripts and the tools that run them.
- [Awesome-WebExtensions](https://github.com/fregante/Awesome-WebExtensions) by fregante - Resources for writing browser extensions.

### CLI and terminal

- [awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) by Julien Le Coupanec - Cheatsheets for languages, frameworks and tools.
- [awesome-cli-apps-in-a-csv](https://github.com/toolleeo/awesome-cli-apps-in-a-csv) by toolleeo - A big table of command line and TUI programs.
- [awesome-cli-frameworks](https://github.com/shadawck/awesome-cli-frameworks) by Shadawck - Libraries for building command line interfaces, by language.
- [awesome-dotfiles](https://github.com/webpro/awesome-dotfiles) by Lars Kappert - Dotfile guides, tools and examples.
- [awesome-nu](https://github.com/nushell/awesome-nu) by Nushell Project - Plugins, scripts and completions for Nushell.
- [awesome-terminals](https://github.com/cdleon/awesome-terminals) by Carlos - Terminal emulators, multiplexers and related tools.
- [awesome-tmux](https://github.com/rothgar/awesome-tmux) by Justin Garrison - Tutorials, configs, themes and plugins for tmux.
- [awesome-tuis](https://github.com/rothgar/awesome-tuis) by Justin Garrison - Terminal user interface projects.
- [awesome-wezterm](https://github.com/michaelbrusegard/awesome-wezterm) by Michael Brusegard - Plugins and configs for the WezTerm terminal.
- [awesome-zellij](https://github.com/zellij-org/awesome-zellij) by zellij-org - Plugins and tools for the Zellij terminal workspace.
- [awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins) by Joe Block - Zsh frameworks, plugins, themes and tutorials.
- [awsm.fish](https://github.com/jorgebucaran/awsm.fish) by Jorge Bucaran - Prompts, plugins and other things for the Fish shell.

### Editors

- [awesome-devcontainers](https://github.com/manekinekko/awesome-devcontainers) by Wassim Chegham - Templates, features and tools for development containers.
- [awesome-emacs](https://github.com/emacs-tw/awesome-emacs) by Emacs.tw - Packages and libraries for Emacs.
- [awesome-neovim](https://github.com/rockerBOO/awesome-neovim) by Dave Lage - Plugins and resources for Neovim.
- [awesome-vim](https://github.com/akrawchyk/awesome-vim) by Andrew Krawchyk - A short list of Vim plugins worth knowing.
- [awesome-vscode](https://github.com/viatsko/awesome-vscode) by Valerii Iatsko - Extensions and resources for VS Code.
- [vim-keybindings-everywhere-the-ultimate-list](https://github.com/erikw/vim-keybindings-everywhere-the-ultimate-list) by Erik Westrup - Which programs support Vim keybindings, natively or through an extension.

### Git and GitHub

- [awesome-badges](https://github.com/badges/awesome-badges) by Shields.io - Badge services, generators and icon sets for READMEs.
- [awesome-git](https://github.com/dictcp/awesome-git) by Dick Tang - Git tools, guides and other useful things.
- [awesome-github](https://github.com/AntBranch/awesome-github) by Ants Open Source On GitHub  - GitHub guides, articles and sites.
- [awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) by Abhishek Naidu - GitHub profile READMEs to borrow ideas from, plus tools to build your own.
- [tips](https://github.com/git-tips/tips) by git-tips - Everyday Git tips and tricks.

### Linux desktop

- [awesome-appimage](https://github.com/AppImageCommunity/awesome-appimage) by AppImage Community - Tools for finding, running, building and updating AppImages.
- [Awesome-Arch](https://github.com/PandaFoss/Awesome-Arch) by Max Ferrer - Distributions and projects built on Arch Linux.
- [awesome-gnome](https://github.com/Kazhnuz/awesome-gnome) by Kazhnuz - Apps, extensions and themes for the GNOME desktop.
- [awesome-hyprland](https://github.com/hyprland-community/awesome-hyprland) by Hyprland Community - Plugins, config tools and add-ons for the Hyprland compositor.
- [awesome-kde](https://github.com/francoism90/awesome-kde) by François M. - Apps, extensions and themes for the KDE Plasma desktop.
- [awesome-ricing](https://github.com/fosslife/awesome-ricing) by fosslife - Window managers, bars, colour schemes and tools for customising a Linux desktop.
- [awesome-wayland](https://github.com/rcalixte/awesome-wayland) by Rick Calixte - Compositors, tools and apps for the Wayland display protocol.

### No-code and low-code

- [awesome-lowcode](https://github.com/antdimot/awesome-lowcode) by Antonio Di Motta - Low-code development platforms, grouped by what they build.
- [awesome-nocode-lowcode](https://github.com/kairichard/awesome-nocode-lowcode) by Kai Richard Koenig - No-code and low-code platforms for building apps, sites and automations.

### Notes and knowledge

- [awesome-anki](https://github.com/tianshanghong/awesome-anki) by wwang - Clients, decks and add-ons for Anki flashcards.
- [awesome-knowledge-management](https://github.com/brettkromkamp/awesome-knowledge-management) by Brett Alistair Kromkamp - People, articles and software on managing knowledge.
- [awesome-logseq](https://github.com/logseq/awesome-logseq) by Logseq - Themes, plugins and workflows for the Logseq notes app.
- [awesome-note-taking](https://github.com/tehtbl/awesome-note-taking) by Thomas - Note-taking and personal knowledge apps, open source and proprietary.
- [awesome-notion](https://github.com/spencerpauly/awesome-notion) by Spencer Pauly - Templates, tools and integrations for Notion.

### Platforms

- [awesome-mac](https://github.com/jaywcjlove/awesome-mac) by 小弟调调 - High quality macOS software, grouped by use.
- [awesome-macadmin-tools](https://github.com/smashism/awesome-macadmin-tools) by emily - Tools for managing Macs across an organisation.
- [awesome-macOS](https://github.com/iCHAIT/awesome-macOS) by Chaitanya Gupta - Applications and tools for macOS.
- [awesome-openbsd-desktop](https://github.com/raffaelschneider/awesome-openbsd-desktop) by Raffael Schneider - Apps and guides for using OpenBSD as a desktop.
- [awesome-powertoys-run-plugins](https://github.com/hlaueriksson/awesome-powertoys-run-plugins) by Henrik Lau Eriksson - Community plugins for the PowerToys Run launcher on Windows.
- [awesome-unix](https://github.com/sirredbeard/awesome-unix) by Hayden Barnes - Linux, BSD, macOS and other Unix-like systems.
- [awesome-windows](https://github.com/0PandaDEV/awesome-windows) by PandaDEV - Tools and apps for Windows.
- [awesome-wsl](https://github.com/sirredbeard/awesome-wsl) by Hayden Barnes - Distributions, tools and guides for Windows Subsystem for Linux.

## Self-hosting

- [awesome-arr](https://github.com/Ravencentric/awesome-arr) by Raventric - Sonarr, Radarr and the related apps for managing a media library.
- [awesome-communication](https://github.com/okhosting/awesome-communication) by Edgard David Iván Muñoz Chávez - Open source chat, video and collaboration tools.
- [awesome-homelab](https://github.com/AwesomeHomelab/awesome-homelab) by AwesomeHomelab - Software, hardware and guides for building a homelab.
- [awesome-jellyfin](https://github.com/awesome-jellyfin/awesome-jellyfin) by awesome-jellyfin - Plugins, themes and clients for the Jellyfin media server.
- [awesome-opensource-email](https://github.com/Mindbaz/awesome-opensource-email) by Mindbaz - Open source mail servers, spam filters, webmail and testing tools.
- [awesome-oss-alternatives](https://github.com/RunaCapital/awesome-oss-alternatives) by Runa Capital - Open source alternatives to popular SaaS products.
- [awesome-proxmox-ve](https://github.com/Corsinvest/awesome-proxmox-ve) by Corsinvest Srl - Tools, backups, monitoring and guides for Proxmox VE.
- [awesome-restic](https://github.com/rubiojr/awesome-restic) by Sergio Rubio - Apps, wrappers and compatible tools for restic backups.
- [awesome-selfhost-docker](https://github.com/hotheadhacker/awesome-selfhost-docker) by Salman Qureshi - Self-hosted apps you can deploy with Docker and Compose.
- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) by awesome-selfhosted - Free software network services and web apps you can host yourself.
- [awesome-startpage](https://github.com/jnmcfly/awesome-startpage) by Jan - Browser start pages and dashboards you can host yourself.
- [awesome-tunneling](https://github.com/anderspitman/awesome-tunneling) by Anders Pitman - Alternatives to ngrok, Cloudflare Tunnel and Tailscale for exposing local services.
- [awesome-webdav](https://github.com/fstanis/awesome-webdav) by Filip Stanis - WebDAV servers, clients and the apps that support it.
- [Compose-Examples](https://github.com/Haxxnet/Compose-Examples) by Haxxnet - Ready-made Docker Compose files for self-hosted services.
- [definitive-opensource](https://github.com/mustbeperfect/definitive-opensource) by Lucas - The best consumer-facing open source apps, by category.
- [Self-Hosting-Guide](https://github.com/mikeroyal/Self-Hosting-Guide) by Michael Royal - A guide to hosting your own services, at home or in the cloud.

## Programming languages

### Across languages

- [awesome-esolangs](https://github.com/angrykoala/awesome-esolangs) by angrykoala - Esoteric programming languages and the people who make them.
- [awesome-programming-languages](https://github.com/ChessMax/awesome-programming-languages) by Журат Максим - Hundreds of programming languages worth a look, with a line on each.

### Ada

- [awesome-ada](https://github.com/ohenley/awesome-ada) by olivier henley - Ada and SPARK tutorials, libraries and tools.

### C and C++

- [awesome-c](https://github.com/oz123/awesome-c) by Oz Tiram - C libraries, frameworks and resources.
- [awesome-cmake](https://github.com/onqtam/awesome-cmake) by Viktor Kirilov - CMake scripts, modules and guides.
- [awesome-cpp](https://github.com/fffaraz/awesome-cpp) by Faraz - C++ (and some C) libraries, frameworks and resources.
- [awesome-hpp](https://github.com/p-ranav/awesome-hpp) by Pranav - Header-only C++ libraries, grouped by job.
- [awesome-llvm](https://github.com/learn-llvm/awesome-llvm) by learn-llvm - LLVM and Clang tools, projects and reading.

### C#

- [awesome-avalonia](https://github.com/AvaloniaCommunity/awesome-avalonia) by Avalonia Community - Libraries, samples and tools for Avalonia UI.
- [awesome-blazor](https://github.com/AdrienTorris/awesome-blazor) by Adrien Torris - Resources for building web apps with Blazor.
- [awesome-dot-net-performance](https://github.com/adamsitnik/awesome-dot-net-performance) by Adam Sitnik - Books, talks and tools for making .NET code faster.
- [awesome-dotnet](https://github.com/quozd/awesome-dotnet) by Vitali Fokin - Libraries, tools and frameworks for the .NET platform.
- [awesome-dotnet-core](https://github.com/thangchung/awesome-dotnet-core) by Thang Chung - Libraries, tools and frameworks for .NET Core.
- [awesome-dotnet-maui](https://github.com/jsuarezruiz/awesome-dotnet-maui) by Javier Suárez - Libraries, samples and books for .NET MAUI.
- [csharp-source-generators](https://github.com/amis92/csharp-source-generators) by Amadeusz Sadowski - C# source generators and articles on writing them.

### Clojure

- [awesome-clojure](https://github.com/razum2um/awesome-clojure) by Vlad Bokov - Clojure libraries and resources.

### Common Lisp

- [awesome-cl](https://github.com/CodyReichert/awesome-cl) by Cody Reichert - Common Lisp frameworks, libraries and resources.
- [awesome-lisp-languages](https://github.com/dundalek/awesome-lisp-languages) by Jakub Dundalek - Lisp-flavoured languages that run on other platforms, compared.

### Crystal

- [awesome-crystal](https://github.com/veelenga/awesome-crystal) by Vitalii Elenhaupt - Crystal libraries, tools and frameworks.

### D

- [awesome-d](https://github.com/dlang-community/awesome-d) by D Community hub - D documents, frameworks and libraries.

### Dart and Flutter

- [awesome-dart](https://github.com/yissachar/awesome-dart) by yissachar - Dart frameworks and libraries.
- [awesome-flutter](https://github.com/Solido/awesome-flutter) by Robert Felker - Flutter libraries, tools and learning material.

### Elixir

- [awesome-elixir](https://github.com/h4cc/awesome-elixir) by Julius Beckmann - Elixir and Erlang libraries and resources.

### Elm

- [awesome-elm](https://github.com/sporto/awesome-elm) by Sebastian Porto - Elm tutorials, libraries and software.

### F#

- [awesome-fsharp](https://github.com/fsprojects/awesome-fsharp) by F# Community Project Incubation Space - F# frameworks, libraries and tools.

### Fortran

- [awesome-fortran](https://github.com/rabbiabram/awesome-fortran) by Vladislav - Modern Fortran libraries, compilers and tools.

### Gleam

- [awesome-gleam](https://github.com/gleam-lang/awesome-gleam) by Gleam - Gleam packages, projects and resources.

### Go

- [awesome-fiber](https://github.com/gofiber/awesome-fiber) by Fiber - Middleware and boilerplates for the Fiber framework.
- [awesome-go](https://github.com/avelino/awesome-go) by Avelino - Go frameworks, libraries and software.
- [go-recipes](https://github.com/nikolaydubina/go-recipes) by Nikolay Dubina - Handy tools and commands for working on Go projects.

### Haskell

- [awesome-haskell](https://github.com/krispo/awesome-haskell) by Konstantin Skipor - Haskell links, frameworks and libraries.

### Java

- [awesome-java](https://github.com/akullpp/awesome-java) by aku - Java frameworks, libraries and software.
- [AwesomeJavaFX](https://github.com/mhrimaz/AwesomeJavaFX) by Hossein Rimaz - JavaFX libraries, books and talks.
- [vertx-awesome](https://github.com/vert-x3/vertx-awesome) by Eclipse Vert.x - Resources and libraries for Vert.x.

### JavaScript and TypeScript

- [33-js-concepts](https://github.com/leonardomso/33-js-concepts) by Leonardo Maldonado - Reading on 33 core JavaScript concepts, from closures to the event loop.
- [awesome-bun](https://github.com/oven-sh/awesome-bun) by Bun - Frameworks, libraries and articles for the Bun runtime.
- [awesome-deno](https://github.com/denolib/awesome-deno) by DenoLib - Things built for and around Deno.
- [awesome-eslint](https://github.com/dustinspecker/awesome-eslint) by Dustin Specker - ESLint plugins and configs.
- [awesome-fp-js](https://github.com/stoeffel/awesome-fp-js) by Christoph Hermann - Functional programming in JavaScript.
- [awesome-javascript](https://github.com/sorrycc/awesome-javascript) by chencheng (云谦) - Browser-side JavaScript libraries and resources.
- [awesome-javascript-learning](https://github.com/micromata/awesome-javascript-learning) by Micromata GmbH - A short list of the best places to learn JavaScript.
- [awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) by Sindre Sorhus - Node.js packages and resources.
- [awesome-npm](https://github.com/sindresorhus/awesome-npm) by Sindre Sorhus - Resources and tips for working with npm.
- [awesome-react-native](https://github.com/jondot/awesome-react-native) by Dotan J. Nahum - React Native components, tools and learning material.
- [awesome-typescript](https://github.com/semlinker/awesome-typescript) by 阿宝哥 - TypeScript resources for the browser and the server.
- [awesome-vite](https://github.com/vitejs/awesome-vite) by Vite - Plugins, templates and integrations for Vite.

### Kotlin

- [awesome-kotlin](https://github.com/Heapy/awesome-kotlin) by Heapy - Kotlin libraries, frameworks and learning material.
- [kmp-awesome](https://github.com/terrakok/kmp-awesome) by Konstantin - Kotlin Multiplatform libraries and tools.

### Mojo

- [awesome-mojo](https://github.com/mojicians/awesome-mojo) by Mojicians - Mojo libraries, apps and learning material.

### Nim

- [awesome-nim](https://github.com/ringabout/awesome-nim) by ringabout - Nim libraries, tools and learning material.

### OCaml

- [awesome-ocaml](https://github.com/ocaml-community/awesome-ocaml) by OCaml Community - OCaml tools, frameworks and libraries.

### Odin

- [awesome-odin](https://github.com/jakubtomsu/awesome-odin) by jakubtomsu - Odin libraries, bindings and tools.

### Pascal and Delphi

- [awesome-pascal](https://github.com/Fr0sT-Brutal/awesome-pascal) by Fr0sT-Brutal - Delphi and Free Pascal libraries and frameworks.

### PHP

- [awesome-php](https://github.com/ziadoz/awesome-php) by Jamie York - PHP libraries, resources and tools.

### Prolog

- [awesome-prolog](https://github.com/klaudiosinani/awesome-prolog) by Klaudio Sinani - Prolog implementations, libraries and learning material.

### Python

- [awesome-asgi](https://github.com/florimondmanca/awesome-asgi) by Florimond Manca - ASGI servers, frameworks and libraries for async Python web apps.
- [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio) by Timo Furrer - Frameworks and libraries built on Python asyncio.
- [awesome-django](https://github.com/wsvincent/awesome-django) by Will Vincent - Django packages, tutorials and tools.
- [awesome-fastapi](https://github.com/mjhea0/awesome-fastapi) by Michael Herman - FastAPI projects and tools.
- [awesome-flask](https://github.com/humiaozuzu/awesome-flask) by Maple - Flask plugins and resources.
- [awesome-flask](https://github.com/mjhea0/awesome-flask) by Michael Herman - Flask extensions and projects.
- [awesome-functional-python](https://github.com/sfermigier/awesome-functional-python) by Stefane Fermigier - Libraries, talks and books on functional programming in Python.
- [awesome-pydantic](https://github.com/jamesonl/awesome-pydantic) by Jameson Lee - Projects built on Pydantic, from CLIs to ML.
- [awesome-python](https://github.com/vinta/awesome-python) by Vinta Chen - Python libraries organised by what you want to do.
- [awesome-python-applications](https://github.com/mahmoud/awesome-python-applications) by Mahmoud Hashemi - Open source apps written in Python, useful as real-world code to read.
- [awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) by Krzysztof Joachimiak - Python software for data science.
- [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing) by TypedDjango - Types, stubs, plugins and tools for typed Python.

### R

- [awesome-R](https://github.com/qinwf/awesome-R) by qinwf - R packages, frameworks and software.

### Roc

- [roc-awesome](https://github.com/lukewilliamboswell/roc-awesome) by Luke Boswell - Packages, platforms and examples for the Roc language.

### Rocq and proof assistants

- [awesome-coq](https://github.com/rocq-community/awesome-coq) by Rocq-community - Libraries, plugins and courses for the Rocq (formerly Coq) proof assistant.

### Ruby

- [awesome-rails](https://github.com/gramantin/awesome-rails) by Gramantin - Libraries and resources for Ruby on Rails.
- [awesome-ruby](https://github.com/markets/awesome-ruby) by Marc Anguera - Ruby libraries, tools and frameworks.
- [learn-ruby](https://github.com/fpsvogel/learn-ruby) by Felipe Vogel - A guided path through Ruby and Rails learning resources.

### Rust

- [awesome-alternatives-in-rust](https://github.com/TaKO8Ki/awesome-alternatives-in-rust) by Takayuki Maeda - Rust rewrites of familiar tools and software.
- [awesome-leptos](https://github.com/leptos-rs/awesome-leptos) by Leptos - Libraries, templates and tools for the Leptos web framework.
- [awesome-ratatui](https://github.com/ratatui/awesome-ratatui) by Ratatui - Apps and libraries built with Ratatui.
- [awesome-rust](https://github.com/rust-unofficial/awesome-rust) by rust-unofficial - Rust code and resources.
- [awesome-yew](https://github.com/jetli/awesome-yew) by Jet Li - Things for building web apps in Rust with Yew.

### Scala

- [awesome-scala-native](https://github.com/tindzk/awesome-scala-native) by Tim Nieradzik - Libraries and tools for compiling Scala to native code.

### Scheme

- [awesome-scheme](https://github.com/schemedoc/awesome-scheme) by Scheme Documentation - Scheme implementations, libraries and books.

### Shell

- [awesome-bash](https://github.com/awesome-lists/awesome-bash) by Awesome - Bash scripts and resources.
- [awesome-shell](https://github.com/alebcay/awesome-shell) by Caleb Xu - Command line frameworks, toolkits and guides.

### Swift

- [awesome-ios](https://github.com/vsouza/awesome-ios) by Vinicius Souza - The iOS ecosystem, including Swift and Objective-C libraries.
- [awesome-swift](https://github.com/matteocrippa/awesome-swift) by Matteo Crippa - Swift libraries and resources.
- [awesome-swiftui](https://github.com/vlondon/awesome-swiftui) by Vladimirs Matusevics - Articles, talks and code examples for SwiftUI.

### V

- [awesome-v](https://github.com/vlang/awesome-v) by The V Programming Language - V frameworks, libraries and software.

### VBA

- [awesome-vba](https://github.com/sancarn/awesome-vba) by Sancarn - Libraries and tools for VBA and VB6.

### Zig

- [awesome-zig](https://github.com/zigcc/awesome-zig) by Zig Chinese Community - Zig libraries and resources.

## Web development

### Backend and servers

- [awesome-adonisjs](https://github.com/adonisjs-community/awesome-adonisjs) by AdonisJS Community - Packages, tutorials and videos for AdonisJS.
- [awesome-express](https://github.com/rajikaimal/awesome-express) by Rajika Imal - Middleware, tools and articles for Express.
- [awesome-json](https://github.com/burningtree/awesome-json) by tree - JSON libraries and resources.
- [awesome-nestjs](https://github.com/nestjs/awesome-nestjs) by nestjs - Libraries, projects and resources for NestJS.
- [awesome-nginx](https://github.com/agile6v/awesome-nginx) by agile6v - Nginx distributions and third-party modules.
- [awesome-websockets](https://github.com/facundofarias/awesome-websockets) by Facundo Farias - WebSocket libraries and tools by language.
- [nginx-resources](https://github.com/fcambus/nginx-resources) by Frederic Cambus - Resources covering Nginx, Lua and OpenResty.

### CSS and graphics

- [awesome-canvas](https://github.com/raphamorim/awesome-canvas) by Raphael Amorim - HTML5 Canvas examples and libraries.
- [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding) by Terkel - Books, courses and tools for generative art and creative coding.
- [awesome-css-frameworks](https://github.com/troxler/awesome-css-frameworks) by troxler - CSS frameworks compared.
- [awesome-css-learning](https://github.com/micromata/awesome-css-learning) by Micromata GmbH - A short list of the best places to learn CSS.
- [awesome-sass](https://github.com/Famolus/awesome-sass) by Famolus - Sass and SCSS frameworks and libraries.
- [awesome-stylelint](https://github.com/stylelint/awesome-stylelint) by Stylelint - Plugins, configs and tools for the Stylelint CSS linter.
- [awesome-svg](https://github.com/willianjusten/awesome-svg) by Willian Justen  - SVG tools, tutorials and examples.
- [awesome-threejs](https://github.com/AxiomeCG/awesome-threejs) by Adam NAILI - Tutorials, shaders and tools for three.js.
- [awesome-typography](https://github.com/Jolg42/awesome-typography) by Joël Galeran - Digital typography resources.
- [awesome-web-animation](https://github.com/sergey-pimenov/awesome-web-animation) by Sergey Pimenov - Libraries and reading for web animation.
- [awesome-webaudio](https://github.com/notthetup/awesome-webaudio) by Chinmay Pendharkar - Web Audio libraries, MIDI tools and tutorials.
- [awesome-webgl](https://github.com/sjfricke/awesome-webgl) by Spencer Fricke - WebGL libraries and learning resources.
- [awesome-webgpu](https://github.com/mikbry/awesome-webgpu) by Mik - Things around the WebGPU ecosystem.
- [css-protips](https://github.com/AllThingsSmitty/css-protips) by Matt Smith - Tips that improve everyday CSS.

### Frameworks and libraries

- [awesome](https://github.com/nuxt/awesome) by Nuxt - Modules, starters and resources for Nuxt.
- [awesome-angular](https://github.com/PatrickJS/awesome-angular) by PatrickJS - Angular resources.
- [awesome-ant-design](https://github.com/websemantics/awesome-ant-design) by Adnan M.Sagar, PhD - Ant Design resources and related projects.
- [awesome-astro](https://github.com/one-aalam/awesome-astro) by Aftab Alam - Themes, integrations and reading for Astro.
- [awesome-htmx](https://github.com/rajasegar/awesome-htmx) by Rajasegar Chandran - Resources for htmx.
- [awesome-jamstack](https://github.com/automata/awesome-jamstack) by Vilson Vieira - Jamstack tools and resources.
- [awesome-lit](https://github.com/web-padawan/awesome-lit) by Serhii Kulykov - Resources for Lit.
- [awesome-nextjs](https://github.com/unicodeveloper/awesome-nextjs) by Prosper Otemuyiwa - Next.js resources and tools.
- [awesome-node-based-uis](https://github.com/xyflow/awesome-node-based-uis) by xyflow - Libraries and apps for node-based editors and flow diagrams.
- [awesome-preact](https://github.com/preactjs/awesome-preact) by Preact - Things built for Preact.
- [awesome-react](https://github.com/enaqx/awesome-react) by Nick Raienko - The React ecosystem.
- [awesome-react-components](https://github.com/brillout/awesome-react-components) by Rom - React components and libraries, grouped by what they do.
- [awesome-react-headless-components](https://github.com/jxom/awesome-react-headless-components) by jxom - Unstyled React components you can style your own way.
- [awesome-shadcn-ui](https://github.com/birobirobiro/awesome-shadcn-ui) by João Inácio Neto - Components, registries and tools built around shadcn/ui.
- [awesome-solid-js](https://github.com/one-aalam/awesome-solid-js) by Aftab Alam - Libraries, tutorials and projects for SolidJS.
- [awesome-storybook](https://github.com/lauthieb/awesome-storybook) by Laurent Thiebault - Storybook add-ons and resources.
- [awesome-svelte](https://github.com/TheComputerM/awesome-svelte) by Mudit Somani - Svelte resources and tools.
- [awesome-sveltekit](https://github.com/janosh/awesome-sveltekit) by Janosh Riebesell - Real sites built with SvelteKit, with links to their code.
- [awesome-tailwindcss](https://github.com/aniftyco/awesome-tailwindcss) by NiftyCo - Tailwind CSS tools, plugins and resources.
- [awesome-ui-component-library](https://github.com/anubhavsrivastava/awesome-ui-component-library) by Anubhav Srivastava - Component libraries for the main front-end frameworks.
- [awesome-vue](https://github.com/vuejs/awesome-vue) by Vue - Vue.js projects and resources.
- [awesome-wagtail](https://github.com/wagtail/awesome-wagtail) by Wagtail - Packages and articles for the Wagtail CMS.
- [awesome-web-components](https://github.com/web-padawan/awesome-web-components) by Serhii Kulykov - Web Components resources.

### Mobile and cross-platform

- [awesome-android](https://github.com/JStumpp/awesome-android) by Jürgen Stumpp - Android packages and resources.
- [awesome-android-ui](https://github.com/wasabeef/awesome-android-ui) by Daichi Furiya - Android UI libraries, each with a preview of what it does.
- [awesome-capacitor](https://github.com/riderx/awesome-capacitor) by Martin DONADIEU - Capacitor plugins and resources.
- [awesome-electron](https://github.com/sindresorhus/awesome-electron) by Sindre Sorhus - Resources for building apps with Electron.
- [awesome-electron-alternatives](https://github.com/sudhakar3697/awesome-electron-alternatives) by Sudhakar Ramasamy - Lighter ways to build desktop apps than Electron, by language.
- [awesome-ionic](https://github.com/Cap-go/awesome-ionic) by Capgo - Ionic resources.
- [awesome-smart-tv](https://github.com/vitalets/awesome-smart-tv) by Vitaliy Potapov - Platforms, frameworks and tools for building Smart TV apps.
- [awesome-tauri](https://github.com/tauri-apps/awesome-tauri) by Tauri - Apps, plugins and guides for Tauri.
- [open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps) by dkhamsing - Open source iOS, watchOS and visionOS apps to learn from.

### Performance and the platform

- [awesome-pwa](https://github.com/hemanth/awesome-pwa) by Hemanth HM - Progressive Web Apps, tools and articles.
- [awesome-wasm](https://github.com/mbasso/awesome-wasm) by Matteo Basso - Things around WebAssembly.
- [awesome-web-performance-budget](https://github.com/pajaydev/awesome-web-performance-budget) by Ajaykumar - Articles, tools and case studies for setting web performance budgets.
- [awesome-wpo](https://github.com/davidsonfellipe/awesome-wpo) by Davidson Fellipe - Web performance optimisation tools and reading.
- [frontend-case-studies](https://github.com/andrew--r/frontend-case-studies) by Andrey Romanov - Talks and articles on how real companies build their frontends.

### Static sites

- [awesome-hugo](https://github.com/theNewDynamic/awesome-hugo) by the New Dynamic - Starters, themes and tools for Hugo.
- [awesome-jekyll](https://github.com/planetjekyll/awesome-jekyll) by Planet Jekyll - Themes, plugins and guides for Jekyll.

## APIs

- [awesome-api-clients](https://github.com/stepci/awesome-api-clients) by Step CI - API client tools, from desktop apps to the command line.
- [awesome-api-devtools](https://github.com/yosriady/awesome-api-devtools) by Yos Riady - Tools for building, documenting and testing JSON APIs.
- [awesome-billing](https://github.com/kdeldycke/awesome-billing) by Kevin Deldycke - Billing and payments knowledge for cloud platforms, from pricing to tax.
- [awesome-graphql](https://github.com/chentsulin/awesome-graphql) by C. T. Lin - GraphQL libraries, tools and resources.
- [awesome-grpc](https://github.com/grpc-ecosystem/awesome-grpc) by gRPC Ecosystem - Resources for gRPC.
- [awesome-openapi3](https://github.com/APIs-guru/awesome-openapi3) by APIs.guru - Projects built around OpenAPI 3.
- [awesome-rest](https://github.com/marmelab/awesome-rest) by marmelab - Resources on RESTful API design.
- [public-apis](https://github.com/public-apis/public-apis) by public-apis - A big directory of free public APIs.
- [security-apis](https://github.com/jaegeral/security-apis) by Alexander J - Public APIs for security work, from threat feeds to scanners.

## Data

### Data analysis

- [awesome](https://github.com/chartjs/awesome) by Chart.js - Plugins, chart types and integrations for Chart.js.
- [awesome-analytics](https://github.com/oxnr/awesome-analytics) by 0xnr - Analytics frameworks and software.
- [awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) by Pavel Grigoryev - Learning material for data analysis, from SQL and statistics to visualisation.
- [awesome-dataviz](https://github.com/hal9ai/awesome-dataviz) by hal9.ai - Data visualisation libraries and tools.
- [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter) by Markus Schanta - Jupyter projects, libraries and tools.
- [awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) by François Briatte - Books, courses and software for network analysis.
- [awesome-pandas](https://github.com/tommyod/awesome-pandas) by Tommy - Courses, talks and libraries for working with pandas.
- [awesome-polars](https://github.com/ddotta/awesome-polars) by Damien Dotta - Talks, plugins and examples for Polars.
- [awesome-shiny-extensions](https://github.com/nanxstats/awesome-shiny-extensions) by Nan Xiao - R and Python packages that extend Shiny apps.
- [awesome-time-series](https://github.com/lmmentel/awesome-time-series) by Lukasz Mentel - Packages, databases and papers for time series data.
- [AwesomeCSV](https://github.com/secretGeek/AwesomeCSV) by Leon Bambrick - Tools for working with CSV files.

### Data engineering

- [awesome-apache-airflow](https://github.com/jghoman/awesome-apache-airflow) by Jakob Homan - Deployment options, tutorials and best practice for Apache Airflow.
- [awesome-bigdata](https://github.com/oxnr/awesome-bigdata) by 0xnr - Big data frameworks and resources.
- [awesome-data-catalogs](https://github.com/opendatadiscovery/awesome-data-catalogs) by Open Data Discovery - Data catalogues and data observability platforms compared.
- [awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering) by Igor Barinov - Data engineering tools for developers.
- [awesome-dbt](https://github.com/Hiflylabs/awesome-dbt) by Hiflylabs Zrt. - Packages and learning material for dbt.
- [awesome-etl](https://github.com/pawl/awesome-etl) by Paul Brown - ETL frameworks, schedulers and tools.
- [awesome-spark](https://github.com/awesome-spark/awesome-spark) by Awesome Spark - Packages and resources for Apache Spark.
- [awesome-streaming](https://github.com/manuzhang/awesome-streaming) by Manu Zhang - Stream processing frameworks and applications.

### Databases

- [awesome-database-design](https://github.com/sujeet-agrahari/awesome-database-design) by Sujeet Agrahari - Tutorials on designing database schemas well.
- [awesome-db-tools](https://github.com/mgramin/awesome-db-tools) by Maksim Gramin - Tools that make working with databases easier.
- [awesome-duckdb](https://github.com/davidgasquez/awesome-duckdb) by David Gasquez - Extensions, clients and tools powered by DuckDB.
- [awesome-graph](https://github.com/jbmusso/awesome-graph) by Jean-Baptiste Musso - Graph databases, triple stores and graph computing tools.
- [awesome-mongodb](https://github.com/ramnes/awesome-mongodb) by Guillaume Gelin - MongoDB libraries and tools.
- [awesome-mysql](https://github.com/shlomi-noach/awesome-mysql) by Shlomi Noach - MySQL software, libraries and resources.
- [awesome-pocketbase](https://github.com/benallfree/awesome-pocketbase) by Ben Allfree - Community resources for PocketBase.
- [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres) by Alara - PostgreSQL software, libraries and resources.
- [awesome-semantic-web](https://github.com/semantalytics/awesome-semantic-web) by Semantalytics - Standards, tools and stores for the semantic web and linked data.
- [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy) by Hong Minhee (洪 民憙) - Tools for SQLAlchemy.
- [awesome-sqlite](https://github.com/planetopendata/awesome-sqlite) by Planet Open Data - SQLite tools, scripts and books.
- [awesome-supabase](https://github.com/lyqht/awesome-supabase) by Estee Tey - Starters and resources for Supabase.
- [awesome-surreal](https://github.com/surrealdb/awesome-surreal) by SurrealDB - Tools, client libraries and apps for SurrealDB.
- [sqlserver-kit](https://github.com/ktaranov/sqlserver-kit) by Konstantin Taranov - Scripts, tools and best practice for Microsoft SQL Server.

### Geospatial

- [Awesome-GEE](https://github.com/opengeos/Awesome-GEE) by Open Geospatial Solutions - Tutorials, libraries and courses for Google Earth Engine.
- [Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) by Eduardo Lacerda - Geospatial tools across remote sensing, web maps and spatial databases.
- [awesome-gis](https://github.com/sshuair/awesome-gis) by sshuair - GIS software, libraries and data sources.
- [awesome-maplibre](https://github.com/maplibre/awesome-maplibre) by MapLibre - Projects that use or support the MapLibre map libraries.
- [awesome-maps](https://github.com/simsieg/awesome-maps) by Simon Siegert - Interesting online maps on every subject from history to weather.
- [awesome-openstreetmap](https://github.com/osmlab/awesome-openstreetmap) by OSM Lab - Editors, tools and services for OpenStreetMap.

### Open data

- [awesome-iiif](https://github.com/IIIF/awesome-iiif) by International Image Interoperability Framework - Viewers, servers and tools for sharing images from libraries and museums with IIIF.
- [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) by AwesomeData - Open datasets grouped by topic.
- [awesome-public-real-time-datasets](https://github.com/bytewax/awesome-public-real-time-datasets) by Bytewax - Free public data streams you can build real-time projects on.
- [awesome-transit](https://github.com/MobilityData/awesome-transit) by MobilityData IO - Transit data standards, APIs, apps and datasets.

## Security

### AI security

- [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by Otto Sulin - Frameworks, labs and tools for securing AI systems.
- [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) by Corca - Papers, tools and projects on attacking and defending LLMs.
- [awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security) by Maciej Pulikowski - Security risks, research and tools for the Model Context Protocol.

### Cloud security

- [awesome-cloud-security](https://github.com/4ndersonLin/awesome-cloud-security) by Anderson Lin - Benchmarks, tools and reading for securing AWS, Azure and GCP.
- [Awesome-CloudSec-Labs](https://github.com/iknowjason/Awesome-CloudSec-Labs) by Jason Ostrom - Free labs and CTFs for learning cloud and Kubernetes security.

### Cryptography

- [awesome-age](https://github.com/FiloSottile/awesome-age) by Filippo Valsorda - Implementations, plugins and tools for the age encryption format.
- [awesome-cryptography](https://github.com/sobolevn/awesome-cryptography) by sobolevn - Cryptography resources and links.
- [awesome-mpc](https://github.com/rdragos/awesome-mpc) by Dragoș Rotaru - Theory, courses and software for multi-party computation.

### Defence and detection

- [awesome-annual-security-reports](https://github.com/jacobdjwilson/awesome-annual-security-reports) by Jacob Wilson - Annual cyber security reports in one place.
- [awesome-detection-engineering](https://github.com/infosecB/awesome-detection-engineering) by Brendan Chamberlain - Detection engineering resources for security teams.
- [awesome-forensics](https://github.com/cugu/awesome-forensics) by Jonas Plum - Forensic analysis tools, from disk imaging to memory and network.
- [awesome-honeypots](https://github.com/paralax/awesome-honeypots) by jose nazario - Honeypot projects and resources.
- [awesome-incident-response](https://github.com/meirwah/awesome-incident-response) by Meir Wahnon - Tools for incident response.
- [awesome-iocs](https://github.com/sroberts/awesome-iocs) by Scott J. Roberts - Sources of indicators of compromise and the tools that use them.
- [awesome-soc](https://github.com/cyb3rxp/awesome-soc) by cyb3rxp - A knowledge base for building and running a security operations centre.
- [awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) by Adel Ka - Threat detection and hunting resources.
- [awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence) by Herman Slatman - Threat intelligence resources.

### Hardware and IoT security

- [awesome-canbus](https://github.com/iDoka/awesome-canbus) by Dmitry Murzinov - Tools and hardware for working with CAN bus.
- [awesome-industrial-protocols](https://github.com/Orange-Cyberdefense/awesome-industrial-protocols) by Orange Cyberdefense - Industrial network protocols and the tools for testing them.
- [awesome-rtc-hacking](https://github.com/EnableSecurity/awesome-rtc-hacking) by Enable Security - Tools and research on the security of VoIP and WebRTC.
- [awesome-vehicle-security](https://github.com/jaredthecoder/awesome-vehicle-security) by Jared M. Smith - Talks, courses and research on vehicle security.

### Offensive security

- [android-security-awesome](https://github.com/ashishb/android-security-awesome) by Ashish Bhatia - Android security tools and resources.
- [awesome-bug-bounty](https://github.com/djadmin/awesome-bug-bounty) by Dheeraj Joshi - Bug bounty programmes, platforms and write-ups.
- [awesome-bugbounty-tools](https://github.com/vavkamil/awesome-bugbounty-tools) by Kamil Vavra - Bug bounty tools, grouped by stage of a hunt.
- [awesome-ctf-resources](https://github.com/devploit/awesome-ctf-resources) by devploit - Tools and platforms for capture the flag competitions.
- [awesome-cyber-security-university](https://github.com/brootware/awesome-cyber-security-university) by Oaker Min - Free learning paths for getting into cyber security.
- [awesome-cyber-skills](https://github.com/joe-shenouda/awesome-cyber-skills) by Joe Shenouda - Places to practise hacking legally, graded by difficulty.
- [awesome-fuzzing](https://github.com/cpuu/awesome-fuzzing) by Jaeyou PARK - Fuzzing resources for finding software bugs.
- [awesome-hacker-search-engines](https://github.com/edoardottt/awesome-hacker-search-engines) by Edoardo Ottavianelli - Search engines for recon, from exposed servers to leaked code.
- [Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) by Hack with GitHub - A collection of awesome lists for hackers and pentesters.
- [Awesome-Hacking-Resources](https://github.com/vitalysim/Awesome-Hacking-Resources) by VS - Courses, practice sites and channels for learning to hack.
- [awesome-osint](https://github.com/jivoi/awesome-osint) by EK_ - Open source intelligence tools and resources.
- [awesome-password-cracking](https://github.com/n0kovo/awesome-password-cracking) by n0kovo - Tools and research on password cracking.
- [awesome-pentest](https://github.com/enaqx/awesome-pentest) by Nick Raienko - Penetration testing resources and tools.
- [awesome-privilege-escalation](https://github.com/m0nad/awesome-privilege-escalation) by Victor Ramos Mello - Privilege escalation techniques and tools for Linux and Windows.
- [awesome-prompt-injection](https://github.com/Joe-B-Security/awesome-prompt-injection) by Joe-B-Security - Learning material on prompt injection against language models.
- [awesome-vulnerable-apps](https://github.com/vavkamil/awesome-vulnerable-apps) by Kamil Vavra - Deliberately vulnerable apps and VMs to practise on.
- [osx-and-ios-security-awesome](https://github.com/ashishb/osx-and-ios-security-awesome) by Ashish Bhatia - Security tools for macOS and iOS.

### Privacy and identity

- [awesome-anti-censorship](https://github.com/danoctavian/awesome-anti-censorship) by Dan Half-Stack Octavian - Open source tools for getting around censorship and surveillance.
- [awesome-auth](https://github.com/casdoor/awesome-auth) by Casdoor - Authentication and authorisation libraries, services and standards.
- [awesome-iam](https://github.com/kdeldycke/awesome-iam) by Kevin Deldycke - Identity and access management knowledge for cloud platforms.
- [awesome-keepass](https://github.com/lgg/awesome-keepass) by Fedor - KeePass clients, plugins and tools across platforms.
- [awesome-openid-connect](https://github.com/cerberauth/awesome-openid-connect) by CerberAuth - OpenID Connect libraries, providers and specs.
- [awesome-privacy](https://github.com/lissy93/awesome-privacy) by Alicia Sykes - Privacy and security focused software and services.
- [awesome-privacy](https://github.com/pluja/awesome-privacy) by pluja - Privacy-respecting services and apps to replace the mainstream ones.
- [awesome-spicedb](https://github.com/authzed/awesome-spicedb) by authzed - Clients, tools and examples for SpiceDB fine-grained permissions.
- [awesome-tor](https://github.com/Polycarbohydrate/awesome-tor) by Polycarbohydrate - Tools, guides and research on the Tor network.
- [awesome-webauthn](https://github.com/yackermann/awesome-webauthn) by Ackermann Yuriy - Libraries, demos and specs for WebAuthn and passkeys.

### Reverse engineering

- [awesome-frida](https://github.com/dweinstein/awesome-frida) by David Weinstein - Libraries, projects and talks for the Frida instrumentation toolkit.
- [awesome-ghidra](https://github.com/AllsafeCyberSecurity/awesome-ghidra) by Allsafe - Scripts, plugins and learning material for Ghidra.
- [awesome-reverse-engineering](https://github.com/morluto/awesome-reverse-engineering) by morluto - Tools and learning paths for reversing binaries, apps and firmware.

### Tools and references

- [awesome-security](https://github.com/sbilly/awesome-security) by sbilly - Security software, libraries, books and other resources.

### Web and application security

- [awesome-burp-extensions](https://github.com/snoopysecurity/awesome-burp-extensions) by Sam Sanoop - Burp Suite extensions, grouped by what they test.
- [awesome-docker-security](https://github.com/myugan/awesome-docker-security) by Muhammad Yuga N. - Docker and container security reading and tools.
- [awesome-dotnet-security](https://github.com/guardrailsio/awesome-dotnet-security) by GuardRails - Tools and reading for securing .NET apps.
- [awesome-graphql-security](https://github.com/Escape-Technologies/awesome-graphql-security) by Escape - Offensive security for the teams that are 100x outnumbered - Resources for securing GraphQL APIs.
- [awesome-nodejs-security](https://github.com/lirantal/awesome-nodejs-security) by Liran Tal - Tools and reading for securing Node.js apps.
- [Awesome-WAF](https://github.com/0xInfection/Awesome-WAF) by Pinaki - How web application firewalls work and how they are tested.
- [awesome-web-security](https://github.com/qazbnm456/awesome-web-security) by Syue Siang Su - Web security materials and resources.
- [WebHackersWeapons](https://github.com/hahwul/WebHackersWeapons) by hahwul - Tools, browser add-ons and proxy extensions used by web hackers.

## Testing and quality

- [awesome-appium](https://github.com/SrinivasanTarget/awesome-appium) by Srinivasan Sekar - Appium resources for mobile testing.
- [awesome-browser-automation](https://github.com/angrykoala/awesome-browser-automation) by angrykoala - Browser automation tools, from Puppeteer to AI agents.
- [awesome-gatling](https://github.com/aliesbelik/awesome-gatling) by Aliaksandr Belik - Plugins, guides and examples for the Gatling load testing tool.
- [awesome-http-benchmark](https://github.com/denji/awesome-http-benchmark) by Denys Denysov - HTTP benchmark and load testing tools.
- [awesome-jest](https://github.com/jest-community/awesome-jest) by Jest Community - Jest packages and resources.
- [awesome-k6](https://github.com/grafana/awesome-k6) by Grafana Labs - Tools and content for k6 load testing.
- [awesome-locust](https://github.com/aliesbelik/awesome-locust) by Aliaksandr Belik - Plugins, guides and examples for the Locust load testing tool.
- [awesome-mutation-testing](https://github.com/theofidry/awesome-mutation-testing) by Théo FIDRY - Mutation testing tools across languages.
- [awesome-playwright](https://github.com/mxschmitt/awesome-playwright) by Max Schmitt - Tools, utilities and projects built with Playwright.
- [awesome-qa](https://github.com/malomarrec/awesome-qa) by Malo Marrec - QA and end-to-end testing tools, from test runners to visual testing.
- [awesome-regression-testing](https://github.com/mojoaxel/awesome-regression-testing) by Alexander Wunschik - Visual regression testing resources.
- [awesome-robotframework](https://github.com/MarketSquare/awesome-robotframework) by marketsquare - Libraries, tools and learning material for Robot Framework.
- [awesome-selenium](https://github.com/christian-bromann/awesome-selenium) by Christian Bromann - Selenium resources.
- [awesome-sites-to-test-on](https://github.com/BMayhew/awesome-sites-to-test-on) by Butch Mayhew - Practice sites for web, API, mobile and security testing.
- [awesome-tap](https://github.com/sindresorhus/awesome-tap) by Sindre Sorhus - Resources for the Test Anything Protocol.
- [awesome-test-automation](https://github.com/atinfo/awesome-test-automation) by at.info - Test automation frameworks and tools, with a page for each language.
- [awesome-testing](https://github.com/TheJambo/awesome-testing) by James Osborn - Testing blogs, talks and tools.
- [awesome-testing-blogs](https://github.com/ChristoWolf/awesome-testing-blogs) by Christoph Wolf - Blogs, newsletters and podcasts on software testing.

## Accessibility

- [awesome-a11y](https://github.com/brunopulis/awesome-a11y) by Bruno Pulis - Accessibility tools, guides and reading.
- [awesome-accessibility](https://github.com/lukeslp/awesome-accessibility) by Luke Steuber - Accessibility resources, tools and best practices, from standards and laws to testing engines, screen reader testing and plain language.
- [awesome-adhd](https://github.com/XargsUK/awesome-adhd) by Brad Duncan - Apps, communities and creators that help with ADHD, from time management to focus.

## Design and UX

- [awesome-ai-tools-for-ui](https://github.com/maxbogo/awesome-ai-tools-for-ui) by Maxim B. - AI tools, skills and MCP servers for UI and UX work.
- [awesome-blender](https://github.com/agmmnn/awesome-blender) by Gökçe - Blender add-ons, tutorials and 3D resources.
- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) by VoltAgent - DESIGN.md files based on well-known brands, for steering AI coding agents.
- [awesome-design-systems](https://github.com/alexpate/awesome-design-systems) by Alex Pate - Design systems from teams around the world.
- [awesome-design-systems](https://github.com/klaufel/awesome-design-systems) by Juan Carlos Ruiz - Bookmarks and articles about design systems.
- [awesome-explorables](https://github.com/blob42/awesome-explorables) by blob42 - Interactive explanations of maths, science and computing.
- [awesome-fonts](https://github.com/brabadu/awesome-fonts) by Boryslav Larin - Free fonts, icon fonts and programming fonts.
- [awesome-framer](https://github.com/podo/awesome-framer) by Giedrius Jaloveckas - Things for prototyping with Framer.
- [awesome-icons](https://github.com/notlmn/awesome-icons) by Laxman Damera - Downloadable SVG, PNG and font icon sets.
- [awesome-pixel-art](https://github.com/Siilwyn/awesome-pixel-art) by Selwyn - Tutorials, tools and inspiration for pixel art.
- [awesome-product-design](https://github.com/ttt30ga/awesome-product-design) by ttt30ga - Bookmarks and articles on product design.
- [awesome-stock-resources](https://github.com/neutraltone/awesome-stock-resources) by Tony Phipps - Free stock photos, video and illustrations, sorted by licence.
- [awesome-styleguides](https://github.com/streamich/awesome-styleguides) by Va Da - Public UI style guides from companies and projects.
- [design-resources-for-developers](https://github.com/bradtraversy/design-resources-for-developers) by Brad Traversy - Design and UI resources for developers, from fonts to colour tools.
- [motion-ui-design](https://github.com/fliptheweb/motion-ui-design) by Artur Kornakov - Inspiration and tools for motion design.
- [typography](https://github.com/deanhume/typography) by Dean - Web typography resources.

## AI and machine learning

### AI coding tools

- [awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) by Andrew Lee - Tools for running many coding agents in parallel.
- [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools) by James Murdza - AI developer tools, from IDEs and terminal agents to code review.
- [awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) by Brad - Terminal AI coding agents and the tools that run them.
- [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) by Adrian Vale - Patterns, evals and tools for building the harness around an AI agent.

### AI safety and governance

- [awesome-ai-eval](https://github.com/Vvkmnn/awesome-ai-eval) by V - Tools, methods and platforms for evaluating how reliable AI systems are.
- [awesome-artificial-intelligence-regulation](https://github.com/EthicalML/awesome-artificial-intelligence-regulation) by The Institute for Ethical Machine Learning - AI guidelines, principles, standards and laws around the world.
- [awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) by Samuel Rincé - Tools and research for measuring and reducing the environmental cost of AI.
- [awesome-llm-interpretability](https://github.com/JShollaj/awesome-llm-interpretability) by Johnny Shollaj - Tools, papers and articles on understanding how LLMs work inside.
- [Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) by ydyjya - Papers and articles on LLM safety, from alignment to jailbreaks.

### Large language models and agents

- [awesome-a2a](https://github.com/ai-boost/awesome-a2a) by Adrian Vale - Agents, servers and clients for the Agent2Agent protocol.
- [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) by VoltAgent - Agent skills from official teams and the community, for many coding agents.
- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) by E2B | Cloud for AI Agents - Autonomous AI agents and the tools behind them.
- [awesome-ai-engineering](https://github.com/dipakkr/awesome-ai-engineering) by Deepak Kumar - Roadmaps, tools and projects for AI engineering, from RAG to agents.
- [awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) by Sindre Sorhus - Apps, tools and articles around ChatGPT.
- [awesome-claude](https://github.com/webfuse-com/awesome-claude) by Webfuse - Official resources, SDKs and community tools for Anthropic Claude.
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) by Really Him - Skills, hooks, commands and other add-ons for Claude Code.
- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) by Composio - Skills and tools for extending Claude workflows.
- [awesome-comfyui](https://github.com/ComfyUI-Workflow/awesome-comfyui) by ComfyUI-Workflow - Custom nodes and workflows for ComfyUI.
- [awesome-copilot](https://github.com/github/awesome-copilot) by GitHub - Community instructions, agents and skills for GitHub Copilot.
- [awesome-dspy](https://github.com/ganarajpr/awesome-dspy) by Ganaraj P R - Tutorials, projects and papers for DSPy.
- [awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) by Piebald - Extensions and resources for Gemini CLI.
- [awesome-gemma](https://github.com/google-gemma/awesome-gemma) by Google Gemma - Tools, fine-tunes and guides for Google's Gemma models.
- [awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) by Steven Van Vaerenbergh - Generative AI projects and services.
- [awesome-langchain](https://github.com/kyrolabs/awesome-langchain) by Kyrolabs - Projects built with LangChain.
- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) by Hannibal046 - Large language model papers, tools and courses.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) by Shubham Saboo - Open source LLM, agent and RAG apps you can run and learn from.
- [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) by TensorChord - Tools for running LLM apps in production.
- [awesome-local-llms](https://github.com/vince-lam/awesome-local-llms) by Vince Lam - A comparison of open source local LLM projects.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) by Frank Fiegel - Model Context Protocol servers.
- [Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) by PromptsLab - Prompt engineering guides, papers and tools.
- [Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) by Daniel Skryseth - Retrieval-augmented generation apps and papers.
- [awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers) by Josh Warwick - Hosted MCP servers you can connect to without running anything locally.
- [awesome-sandbox](https://github.com/restyler/awesome-sandbox) by restyler - Sandboxes for running AI-generated code safely, compared.
- [awesome-spring-ai](https://github.com/spring-ai-community/awesome-spring-ai) by spring-ai-community - Tools and examples for building AI apps with Spring AI.
- [awesome-whisper](https://github.com/sindresorhus/awesome-whisper) by Sindre Sorhus - Tools and apps built on Whisper speech recognition.
- [prompts.chat](https://github.com/f/prompts.chat) by Fatih Kadir Akın - Prompts to share, find and reuse with chat models.

### Machine learning and data science

- [awesome-artificial-intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) by Owain Lewis - AI courses, books and papers.
- [awesome-AutoML](https://github.com/windmaple/awesome-AutoML) by Wayne Wei - AutoML research, tools and projects.
- [awesome-colab-notebooks](https://github.com/amrzv/awesome-colab-notebooks) by Alexey Morozov - Colab notebooks for courses and research projects you can run in a browser.
- [Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models) by Kedan Li - Ready-to-use Core ML models for Apple platforms.
- [awesome-datascience](https://github.com/academic/awesome-datascience) by Academic.io - Data science material to learn from and apply.
- [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) by Chris - Deep learning tutorials, projects and communities.
- [awesome-deep-rl](https://github.com/kengz/awesome-deep-rl) by Keng - Libraries, environments and tutorials for deep reinforcement learning.
- [awesome-full-stack-machine-learning-courses](https://github.com/leehanchung/awesome-full-stack-machine-learning-courses) by Han - Free university courses on machine learning engineering.
- [awesome-jax](https://github.com/n2cholas/awesome-jax) by Nicholas Vadivelu - JAX libraries and learning material.
- [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) by Joseph Misiti - Machine learning frameworks and libraries by language.
- [awesome-mlops](https://github.com/kelvins/awesome-mlops) by Kelvin S. do Prado - MLOps tools and practices.
- [awesome-nlp](https://github.com/keon/awesome-nlp) by Keon - Natural language processing resources.
- [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) by The Institute for Ethical Machine Learning - Open source tools to deploy, monitor and scale machine learning.
- [Awesome-pytorch-list](https://github.com/bharathgs/Awesome-pytorch-list) by bharath g s - PyTorch libraries, papers and tutorials.
- [awesome-tensorflow](https://github.com/jtoy/awesome-tensorflow) by jtoy - TensorFlow resources.
- [awesomeMLSys](https://github.com/gpu-mode/awesomeMLSys) by GPU MODE - A reading list for getting started in ML systems.
- [techniques](https://github.com/satellite-image-deep-learning/techniques) by satellite-image-deep-learning - Deep learning techniques for satellite and aerial imagery.

### Research and models

- [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) by PolyU X AI Lab - Surveys, papers and projects on graph-based retrieval.
- [Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) by xlite-dev - Papers with code on making LLM inference faster and cheaper.
- [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) by Armando Fortes - Papers on reasoning in LLMs, from chain of thought to reasoning models.
- [Awesome-Model-Quantization](https://github.com/AI-Efficiency/Awesome-Model-Quantization) by Efficient Intelligence and Systems (EIS) Lab - Papers, benchmarks and tools for model quantisation.
- [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) by BradyFU - Papers, datasets and benchmarks for multimodal LLMs.
- [Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) by eosphoros - Tutorials, models and benchmarks for turning questions into SQL.

## Documentation and technical writing

- [awesome-devrel](https://github.com/devrelcollective/awesome-devrel) by DevRel Collective - Tools and reading for developer relations work.
- [awesome-docs](https://github.com/testthedocs/awesome-docs) by TestTheDocs - Incubator - Tools for writing and testing documentation.
- [awesome-docsify](https://github.com/docsifyjs/awesome-docsify) by docsifyjs - Plugins, themes and showcases for docsify.
- [awesome-graphviz](https://github.com/dbt4u/awesome-graphviz) by Detlef Burkhardt - Tools, bindings and editors for drawing diagrams with Graphviz.
- [awesome-LaTeX](https://github.com/egeerardyn/awesome-LaTeX) by Egon Geerardyn - LaTeX tools, packages and guides.
- [awesome-markdown](https://github.com/mundimark/awesome-markdown) by Mundi Mark - Markdown flavours, tools and extensions.
- [awesome-marp](https://github.com/marp-team/awesome-marp) by Marp - Themes, tools and examples for making slides in Markdown with Marp.
- [awesome-quarto](https://github.com/mcanouil/awesome-quarto) by Mickaël Canouil - Quarto talks, tools and examples.
- [awesome-readme](https://github.com/matiassingers/awesome-readme) by Matias Singers - READMEs worth copying ideas from.
- [awesome-scientific-writing](https://github.com/writing-resources/awesome-scientific-writing) by writing-resources - Tools and demos for scientific writing.
- [awesome-sphinxdoc](https://github.com/ygzgxyz/awesome-sphinxdoc) by Hyunjun Kim - Sphinx themes, extensions and guides.
- [awesome-technical-writing](https://github.com/BolajiAyodeji/awesome-technical-writing) by Bolaji Ayodeji - Articles, books and videos for technical writers.
- [awesome-thesis](https://github.com/awesome-thesis/awesome-thesis) by awesome-thesis - Practical tips for writing a computer science thesis.
- [awesome-tikz](https://github.com/xiaohanyu/awesome-tikz) by Xiao Hanyu - Documentation and libraries for drawing with TikZ.
- [awesome-typst](https://github.com/qjcg/awesome-typst) by John Gosset - Templates, packages and tools for the Typst typesetting system.
- [beautiful-docs](https://github.com/matheusfelipeog/beautiful-docs) by Matheus Felipe - Examples of clear, well-made documentation.

## Hardware and embedded

### Boards and microcontrollers

- [awesome-circuitpython](https://github.com/adafruit/awesome-circuitpython) by Adafruit Industries - CircuitPython guides, libraries and projects.
- [Awesome-Embedded](https://github.com/nhivp/Awesome-Embedded) by Nhi Pham - Embedded programming resources.
- [awesome-embedded-rust](https://github.com/rust-embedded/awesome-embedded-rust) by Rust Embedded - Embedded and low-level Rust resources.
- [awesome-embedded-software](https://github.com/iDoka/awesome-embedded-software) by Dmitry Murzinov - Libraries and protocols that suit small embedded systems.
- [awesome-esp](https://github.com/agucova/awesome-esp) by Agustín Covarrubias - ESP8266 and ESP32 projects and code.
- [awesome-esp-rust](https://github.com/esp-rs/awesome-esp-rust) by esp-rs - Rust tools, books and templates for ESP32 chips.
- [awesome-microbit](https://github.com/carlosperate/awesome-microbit) by Carlos Pereira Atencio - Editors, extensions and projects for the BBC micro:bit.
- [awesome-micropython](https://github.com/mcauser/awesome-micropython) by Mike Causer - MicroPython libraries and frameworks.
- [awesome-raspberry-pi](https://github.com/thibmaek/awesome-raspberry-pi) by Thibault Maekelbergh - Raspberry Pi tools and projects.

### Devices and gadgets

- [awesome-flying-fpv](https://github.com/Matthias84/awesome-flying-fpv) by Matthias84 - Open hardware and software for building drones and RC planes.
- [awesome-plotters](https://github.com/beardicus/awesome-plotters) by Brian Boucheron - Hardware and software for pen plotters and drawing robots.
- [awesome-reMarkable](https://github.com/reHackable/awesome-reMarkable) by reHackable - Apps, tools and hacks for the reMarkable tablet.

### Electronics and chips

- [awesome-electronics](https://github.com/kitspace/awesome-electronics) by kitspace - Electronics engineering resources.
- [awesome-hdl](https://github.com/drom/awesome-hdl) by Aliaksei Chapyzhenka - Hardware description languages, simulators and synthesis tools.

### IoT, networks and radio

- [awesome-5g](https://github.com/calee0219/awesome-5g) by Chia-An Lee - Open 5G cores, radio access networks and test tools.
- [awesome-edge-computing](https://github.com/qijianpeng/awesome-edge-computing) by QI Jianpeng - Edge computing frameworks, simulators and papers.
- [awesome-gnss](https://github.com/barbeau/awesome-gnss) by Sean Barbeau - Open source GNSS apps, tools and libraries.
- [awesome-iot](https://github.com/HQarroum/awesome-iot) by Halim Qarroum - Internet of Things projects and tools.
- [awesome-mqtt](https://github.com/awesome-mqtt/awesome-mqtt) by awesome-mqtt - MQTT brokers, clients and tools.
- [awesome-netbox](https://github.com/osism/awesome-netbox) by OSISM - Plugins, scripts and integrations for the NetBox network source of truth.
- [awesome-networking](https://github.com/facyber/awesome-networking) by Marko Andrejić - Courses, books and tools for computer networking.
- [awesome-telco](https://github.com/ravens/awesome-telco) by Yan Grunenberger - A guided way into telecoms, from mobile network basics to running your own core.

### Performance and HPC

- [awesome-high-performance-computing](https://github.com/trevor-vincent/awesome-high-performance-computing) by Trevor Vincent - Software, courses and reading on high performance computing.
- [awesome-lockfree](https://github.com/rigtorp/awesome-lockfree) by Erik Rigtorp - Libraries, papers and talks on lock-free programming.
- [cpu-performance-engineering](https://github.com/usamahz/cpu-performance-engineering) by usamahz - A reading path through CPU performance, using primary sources.

### Robotics

- [awesome-robotics-libraries](https://github.com/jslee02/awesome-robotics-libraries) by Jeongseok (JS) Lee - Robotics libraries, from middleware to simulation and planning.
- [awesome-robotics-projects](https://github.com/mjyc/awesome-robotics-projects) by Mike Chung - Open source and affordable robots and the tools behind them.
- [awesome-weekly-robotics](https://github.com/msadowski/awesome-weekly-robotics) by Mateusz Sadowski - Open robots and tools featured in the Weekly Robotics newsletter.

## Games

### Engines and frameworks

- [awesome-flame](https://github.com/flame-engine/awesome-flame) by Flame Engine - Games, libraries and tutorials for the Flame engine for Flutter.
- [awesome-gamemaker](https://github.com/bytecauldron/awesome-gamemaker) by bytecauldron - Libraries, snippets and guides for GameMaker.
- [awesome-godot](https://github.com/Calinou/awesome-godot) by Hugo Locurcio - Free plugins, demos and templates for Godot.
- [awesome-love2d](https://github.com/love2d-community/awesome-love2d) by LÖVE Community - Libraries and tools for the LÖVE framework.
- [awesome-monogame](https://github.com/aloisdeniel/awesome-monogame) by Aloïs Deniel - Libraries and tools for MonoGame.
- [awesome-rust-gamedev](https://github.com/NightsWatchGames/awesome-rust-gamedev) by Night's Watch Games - Engines, libraries and tutorials for making games in Rust.
- [awesome-unity3d](https://github.com/insthync/awesome-unity3d) by Ittipon Teerapruettikulchai - Open source Unity projects and packages by category.
- [awesome-unreal](https://github.com/insthync/awesome-unreal) by Ittipon Teerapruettikulchai - Open source Unreal Engine plugins and projects by category.

### Game development

- [awesome-entity-component-system](https://github.com/jslee02/awesome-entity-component-system) by Jeongseok (JS) Lee - Entity component system libraries and reading.
- [awesome-game-design](https://github.com/Roobyx/awesome-game-design) by Marian Radev - Game design documents, pitches and learning material.
- [awesome-game-engine-dev](https://github.com/stevinz/awesome-game-engine-dev) by Stephens Nunnally - Game engines and the reading behind building one.
- [awesome-steam](https://github.com/scholtzm/awesome-steam) by Michael Scholtz - Libraries, APIs and tools for building on Steam.
- [magictools](https://github.com/ellisonleao/magictools) by Ellison - Tools and assets for game development, from art to audio and engines.
- [MultiplayerNetworkingResources](https://github.com/0xFA11/MultiplayerNetworkingResources) by Fatih Mar - Articles, talks and libraries on multiplayer game networking.

### Open source games

- [awesome-game-remakes](https://github.com/radek-sprta/awesome-game-remakes) by radek-sprta - Open source remakes of classic games that are still maintained.
- [awesome-programming-games](https://github.com/readyready15728/awesome-programming-games) by Lynn Bradshaw - Games where you write code to play.
- [open-source-games](https://github.com/bobeff/open-source-games) by Ivan Bobev - Open source games by genre, including remakes of classics.

### Retro and fantasy consoles

- [awesome-emulators](https://github.com/DerekTurtleRoe/awesome-emulators) by Derek "Turtle" Roe - Emulators for consoles, handhelds and computers.
- [awesome-gbdev](https://github.com/gbdev/awesome-gbdev) by gbdev - Tools, docs and homebrew for making Game Boy games.
- [awesome-PICO-8](https://github.com/pico-8/awesome-PICO-8) by PICO-8 - Carts, tools and tutorials for the PICO-8 fantasy console.

## Media and creative

### Audio and video

- [awesome-broadcasting](https://github.com/ebu/awesome-broadcasting) by European Broadcasting Union - Open source tools for broadcast production and playout.
- [awesome-ffmpeg](https://github.com/transitive-bullshit/awesome-ffmpeg) by Travis Fischer - FFmpeg docs, wrappers and tutorials.
- [awesome-mpv](https://github.com/stax76/awesome-mpv) by stax76 - Front ends, scripts and add-ons for the mpv player.
- [awesome-video](https://github.com/krzemienski/awesome-video) by Nick Krzemienski - Streaming video tools, codecs, players and learning material.

### Graphics and 3D

- [awesome-cg-vfx-pipeline](https://github.com/cgwire/awesome-cg-vfx-pipeline) by CGWire - Open source tools for building a CG and VFX production pipeline.
- [awesome-opengl](https://github.com/eug/awesome-opengl) by Eugênio Cabral - OpenGL libraries, debuggers and tutorials.
- [awesome-OpenSourcePhotography](https://github.com/ibaaj/awesome-OpenSourcePhotography) by Ismaïl Baaj - Open source software and camera mods for photography.
- [awesome-openusd](https://github.com/matiascodesal/awesome-openusd) by matiascodesal - Learning material and tools for OpenUSD.
- [awesome-vulkan](https://github.com/vinjn/awesome-vulkan) by Jing Zhang - Vulkan SDKs, tutorials, samples and tools.

### Music

- [awesome-juce](https://github.com/sudara/awesome-juce) by Sudara - JUCE modules, templates and open source plugins.
- [awesome-music](https://github.com/noteflakes/awesome-music) by Sharon Rosner - Software for audio editing, notation, MIDI and music theory.
- [awesome-musicdsp](https://github.com/olilarkin/awesome-musicdsp) by Oli Larkin - Frameworks and reading for audio and music DSP programming.
- [diy-synths](https://github.com/Atarity/diy-synths) by Misha Sannikov - Open source synthesisers you can build yourself.

## Science and research

- [awesome-agriculture](https://github.com/brycejohnston/awesome-agriculture) by bryce - Open source technology for farming and growing food.
- [awesome-astronomy](https://github.com/jonathansick/awesome-astronomy) by Jonathan Sick - Astronomy software, datasets and blogs.
- [awesome-bci](https://github.com/NeuroTechX/awesome-bci) by NeuroTechX - Software, hardware and datasets for brain-computer interfaces.
- [Awesome-Bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics) by Daniel E Cook - Bioinformatics software and libraries.
- [awesome-cern](https://github.com/CERN/awesome-cern) by European Organization for Nuclear Research - Open source software from CERN, from physics tools to everyday services.
- [awesome-climate-change](https://github.com/stevematthew/awesome-climate-change) by Stephen Matthew - Data, tools and reading on climate change.
- [awesome-computational-social-science](https://github.com/gesiscss/awesome-computational-social-science) by GESIS – Leibniz Institute for the Social Sciences - Courses, books and tools for computational social science.
- [awesome-control-theory](https://github.com/A-make/awesome-control-theory) by A-make - Books, courses and tools for learning control theory.
- [awesome-earth](https://github.com/philsturgeon/awesome-earth) by Phil Sturgeon - Practical things people and teams can do about the climate crisis.
- [awesome-materials-informatics](https://github.com/tilde-lab/awesome-materials-informatics) by Tilde - Software, data and efforts in materials informatics.
- [awesome-math](https://github.com/rossant/awesome-math) by Cyrille Rossant - Courses, books and tools for learning mathematics.
- [awesome-neuroimaging](https://github.com/NPACore/awesome-neuroimaging) by NPACore - Tools for organising and analysing brain imaging data.
- [awesome-neuroscience](https://github.com/analyticalmonk/awesome-neuroscience) by Akash Tandon - Neuroscience libraries, software and learning material.
- [awesome-nuclear](https://github.com/paulromano/awesome-nuclear) by Paul Romano - Open source software for nuclear science and engineering.
- [awesome-open-climate-science](https://github.com/pangeo-data/awesome-open-climate-science) by Pangeo - Open software for climate, ocean and atmospheric science.
- [awesome-open-geoscience](https://github.com/softwareunderground/awesome-open-geoscience) by Software Underground - Open source software and data for geoscience.
- [awesome-optimization](https://github.com/ebrahimpichka/awesome-optimization) by Ebrahim Pichka - Courses and software for mathematical optimisation.
- [awesome-PhD](https://github.com/helenahartmann/awesome-PhD) by Helena Hartmann - Resources for doing a PhD, from writing and funding to wellbeing.
- [awesome-python-chemistry](https://github.com/lmmentel/awesome-python-chemistry) by Lukasz Mentel - Python packages for chemistry.
- [awesome-quantum-software](https://github.com/qosf/awesome-quantum-software) by Quantum Open Source Foundation - Open source quantum computing software.
- [awesome-research](https://github.com/emptymalei/awesome-research) by LM - Tools that help researchers organise reading, writing and data.
- [awesome-scientific-computing](https://github.com/nschloe/awesome-scientific-computing) by Nico Schlömer - Software for numerical analysis and scientific computing.
- [awesome-single-cell](https://github.com/seandavi/awesome-single-cell) by Sean Davis - Software and data for single-cell analysis.
- [awesome-space](https://github.com/orbitalindex/awesome-space) by The Orbital Index - Space-related software, APIs and data.
- [awesome-theoretical-computer-science](https://github.com/mostafatouny/awesome-theoretical-computer-science) by Mostafa Touny - Lecture notes and books on theoretical computer science.
- [awesome-zotero](https://github.com/MohamedElashri/awesome-zotero) by Mohamed Elashri - Plugins, styles and tools for the Zotero reference manager.
- [open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) by protontypes - Open source projects on climate, clean energy and biodiversity.

## Decentralised web

- [awesome-bitcoin](https://github.com/igorbarinov/awesome-bitcoin) by Igor Barinov - Bitcoin services and tools for developers.
- [awesome-bluesky](https://github.com/fishttp/awesome-bluesky) by fishttp - Tools, feeds and clients for Bluesky.
- [awesome-decentralized-web](https://github.com/gdamdam/awesome-decentralized-web) by gio - Peer-to-peer, federated and local-first protocols and apps, with crypto left out.
- [awesome-ipfs](https://github.com/ipfs/awesome-ipfs) by IPFS Project - Apps, tools and services built on IPFS.
- [awesome-noir](https://github.com/noir-lang/awesome-noir) by noir-lang - Libraries, tools and learning material for the Noir zero-knowledge language.
- [awesome-nostr](https://github.com/aljazceru/awesome-nostr) by Aljaz - Clients, relays and tools for the Nostr protocol.
- [awesome-solidity](https://github.com/bkrem/awesome-solidity) by Ben Kremer - Solidity resources, libraries and tools.

## Business and careers

### Finance and trading

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) by Wilson Freitas - Libraries and resources for quantitative finance, by language.
- [awesome-sustainable-finance](https://github.com/open-risk/awesome-sustainable-finance) by Open Risk - Software and data for sustainable finance and climate risk.
- [awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) by Papers With Backtest - Libraries, strategies and books for systematic trading.

### Jobs and remote work

- [awesome-job-boards](https://github.com/emredurukn/awesome-job-boards) by Emre Durukan - Job boards grouped by field, from AI to design and security.
- [awesome-remote-job](https://github.com/lukasz-madon/awesome-remote-job) by Lukasz - Remote jobs and resources for working remotely.
- [awesome-RemoteWork](https://github.com/hugo53/awesome-RemoteWork) by Hoang Nguyen - Books, hiring sites and tools for working remotely.
- [open-source-jobs](https://github.com/timqian/open-source-jobs) by Tim Qian - Open source projects that also offer paid jobs.

### Leadership and management

- [awesome-cto](https://github.com/kuchin/awesome-cto) by Dima Kuchin - An opinionated reading list for CTOs, with an eye on startups.
- [awesome-engineering-management](https://github.com/engineering-management/awesome-engineering-management) by Engineering Management - Models, methods and tools for managing engineering teams.
- [awesome-engineering-strategy](https://github.com/aleixmorgadas/awesome-engineering-strategy) by Aleix Morgadas - Designing and running engineering strategy.
- [awesome-engineering-team-management](https://github.com/kdeldycke/awesome-engineering-team-management) by Kevin Deldycke - Moving from developer to engineering manager.
- [awesome-product-management](https://github.com/dend/awesome-product-management) by Den - Resources for product and programme managers.
- [awesome-project-management](https://github.com/shahedbd/awesome-project-management) by R M Shahidul Islam Shahed - Project management tools, templates and methods.

### Open source and community

- [awesome-ospo](https://github.com/todogroup/awesome-ospo) by TODO (OSPO) Group - Tools for running an open source programme office.
- [awesome-oss](https://github.com/sereneblue/awesome-oss) by sereneblue - Open source projects you can contribute to or donate to.
- [awesome-software-patreons](https://github.com/uraimo/awesome-software-patreons) by uraimo - Developers and open source projects you can support with a regular donation.
- [lemonade-stand](https://github.com/nayafia/lemonade-stand) by Nadia - Ways to fund open source work, with examples of each.
- [tech-coops](https://github.com/hng/tech-coops) by Henning - Worker-owned tech co-operatives and how they work.

### Startups and indie

- [awesome-legal](https://github.com/ankane/awesome-legal) by Andrew Kane - Free legal templates for companies, from privacy policies to founder agreements.
- [awesome-startup](https://github.com/KrishMunot/awesome-startup) by Krish Munot - Books, essays and tools for starting a company.

## General

### Everyday apps and sites

- [awesome-developer-first](https://github.com/agamm/awesome-developer-first) by Agam More - Developer-first tools and products.
- [awesome-free-apps](https://github.com/Axorax/awesome-free-apps) by Axorax - Free apps for desktop and mobile, by category.
- [awesome-useful-websites](https://github.com/atakanaltok/awesome-useful-websites) by Atakan - Useful websites for everyday tasks, from diagrams to file conversion.
- [ToolsOfTheTrade](https://github.com/cjbarber/ToolsOfTheTrade) by Chris Barber - Tools of the trade, as shared on Hacker News.

### Inclusion and wellbeing

- [awesome-transgender](https://github.com/cvyl/awesome-transgender) by Mikka - Resources for transgender people, from health and legal guidance to community.

### Indexes of lists

- [awesome](https://github.com/sindresorhus/awesome) by Sindre Sorhus - The main index of awesome lists.
- [lists](https://github.com/jnv/lists) by Jan Vlnas - Collections of lists curated on GitHub and elsewhere.

### Learning

- [awesome-advent-of-code](https://github.com/Bogdanp/awesome-advent-of-code) by Bogdan Popa - Tools, templates and solutions for Advent of Code.
- [awesome-algorithms](https://github.com/tayllan/awesome-algorithms) by Tayllan Búrigo - Places to learn and practise algorithms.
- [awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) by Shmavon Gazanchyan - Beginner-friendly projects to make a first contribution to.
- [awesome-games-of-coding](https://github.com/michelpereira/awesome-games-of-coding) by Michel Pereira - Games that teach a programming language as you play.
- [awesome-learn-by-playing](https://github.com/lmammino/awesome-learn-by-playing) by Luciano Mammino - Games that teach CSS, Git, SQL, regex and more.
- [awesome-roadmaps](https://github.com/liuchong/awesome-roadmaps) by 刘冲 - Roadmaps for learning many technologies.
- [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) by CodeCrafters - Step-by-step guides to building your own database, Git, shell and more.
- [coding-interview-university](https://github.com/jwasham/coding-interview-university) by John Washam - A long study plan for computer science fundamentals, built for interview preparation.
- [computer-science](https://github.com/ossu/computer-science) by Open Source Society University - A free, self-taught path through computer science.
- [cs-video-courses](https://github.com/Developer-Y/cs-video-courses) by Developer-Y - Recorded university computer science courses, grouped by subject.
- [every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know) by MTDV - Reading on things every developer runs into, from Unicode and time to security.
- [free-programming-books](https://github.com/EbookFoundation/free-programming-books) by Free Ebook Foundation - Free programming books and courses.
- [learn-to-program](https://github.com/karlhorky/learn-to-program) by Karl Horky - Free resources for learning to program, from beginner to advanced.
- [papers-we-love](https://github.com/papers-we-love/papers-we-love) by Papers We Love - Computer science papers worth reading and discussing.
- [programming-math-science](https://github.com/bobeff/programming-math-science) by Ivan Bobev - Free learning resources on programming, maths and science.

### Practice and conventions

- [awesome-falsehood](https://github.com/kdeldycke/awesome-falsehood) by Kevin Deldycke - Falsehoods programmers believe about names, time, addresses and more.
- [awesome-guidelines](https://github.com/Kristories/awesome-guidelines) by W Kristianto - Style guides and coding conventions for many languages and tools.
- [awesome-i18n](https://github.com/oh-jon-paul/awesome-i18n) by Jon Paul - Internationalisation resources for many languages.
- [awesome-naming](https://github.com/gruhn/awesome-naming) by Niklas Gruhn - Well-chosen names in computing and the stories behind them.
- [awesome-regex](https://github.com/slevithan/awesome-regex) by Steven Levithan - Regex tools, tutorials and libraries.
- [awesome-seo](https://github.com/teles/awesome-seo) by Teles - Search engine optimisation resources.
- [awesome-speaking](https://github.com/matteofigus/awesome-speaking) by Matteo Figus - Books, talks and calls for papers for public speaking.
- [awesome-uses](https://github.com/wesbos/awesome-uses) by Wes Bos - Developers' /uses pages showing their setups, gear and software.
- [awesome-web-archiving](https://github.com/iipc/awesome-web-archiving) by IIPC - Tools, standards and training for archiving the web.

### Reading, watching and listening

- [awesome-discord-communities](https://github.com/mhxion/awesome-discord-communities) by Mahadi Xion - Discord communities for programmers, by topic.
- [awesome-engineering-articles](https://github.com/ashishps1/awesome-engineering-articles) by Ashish Pratap Singh - Engineering blog posts from tech companies, grouped by company.
- [awesome-geek-podcasts](https://github.com/ayr-ton/awesome-geek-podcasts) by Ayrton Freeman - Tech podcasts in many languages.
- [awesome-newsletters](https://github.com/zudochkin/awesome-newsletters) by Dmitry Zudochkin - Newsletters on web development, programming and design.
- [awesome-talks](https://github.com/JanVanRyswyck/awesome-talks) by Jan Van Ryswyck - Online talks and screencasts for developers.
- [awesome-youtubers](https://github.com/JoseDeFreitas/awesome-youtubers) by Jose de Freitas - YouTube channels that teach programming and computer science.

### Schools and education

- [awesome-opensource-school](https://github.com/zefanja/awesome-opensource-school) by zefanja - Free and open source software for classrooms and school servers, grouped by subject.

## What qualifies

A list is added when it is curated, maintained, established, public and distinct.

**Curated.** Each item has a short description or a reason for being there. A plain link dump does not count.

**Maintained.** It is not archived and has been pushed to in the last 18 months.

**Established.** It has 500 or more stars, or it is the best list in a small niche. The floor is 25 stars.

**Public on GitHub.** The weekly health check reads GitHub repos.

**Distinct.** It covers something the other entries in its section do not. Each sub-section aims for no more than three.

## How it stays fresh

Every Monday a workflow checks every link in this file, and another checks every GitHub repo it points to. If a link breaks, or a list is archived, gone, quiet for more than 18 months or under 25 stars, an issue opens so it can be fixed or removed. When everything is healthy again the issue closes by itself.

## Contributing

Know a list that belongs here? Open a pull request or use the "Suggest a list" issue form. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first: it covers the right section, alphabetical order and the format line.

Released under [CC0 1.0](LICENSE): to the extent possible under law, the authors have waived all copyright and related rights to this list.
