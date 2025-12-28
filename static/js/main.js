// static/js/main.js
document.addEventListener('DOMContentLoaded', function() {

    // --- PDF DOWNLOAD LOGIC ---
    const downloadBtn = document.getElementById('download-pdf-btn');
    if(downloadBtn) {
        downloadBtn.addEventListener('click', () => {
            const content = document.getElementById('resume-preview-content');
            const personalDetails = content.querySelector('.preview-hero h1');
            const filename = personalDetails ? `${personalDetails.innerText.replace(/ /g, '_')}_Resume.pdf` : 'resume.pdf';

            const options = {
                margin:       [0.5, 0.5, 0.5, 0.5],
                filename:     filename,
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2, useCORS: true },
                jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
            };
            downloadBtn.innerText = "Generating...";
            downloadBtn.disabled = true;
            html2pdf().set(options).from(content).save().then(() => {
                downloadBtn.innerText = "Download as PDF";
                downloadBtn.disabled = false;
            });
        });
    }

    // --- EDUCATION MODAL LOGIC ---
    const eduModal = document.getElementById('editEducationModal');
    if (eduModal) {
        const modalForm = eduModal.querySelector('#editEducationForm');
        const editButtons = document.querySelectorAll('.btn-edit-education');
        const closeButton = eduModal.querySelector('.close-modal-btn');
        const overlay = eduModal.closest('.modal-overlay');

        editButtons.forEach(button => {
            button.addEventListener('click', () => {
                const entryDiv = button.closest('.form-entry');
                const entryId = entryDiv.dataset.entryId;
                modalForm.action = `/update-education/${entryId}/`;
                eduModal.querySelector('#id_institution').value = entryDiv.dataset.institution;
                eduModal.querySelector('#id_degree').value = entryDiv.dataset.degree;
                eduModal.querySelector('#id_start_date').value = entryDiv.dataset.startDate;
                eduModal.querySelector('#id_end_date').value = entryDiv.dataset.endDate;
                overlay.style.display = 'flex';
            });
        });
        const closeEduModal = () => { overlay.style.display = 'none'; };
        closeButton.addEventListener('click', closeEduModal);
        overlay.addEventListener('click', e => { if (e.target === overlay) closeEduModal(); });
    }

    // --- EXPERIENCE MODAL LOGIC ---
    const expModal = document.getElementById('editExperienceModal');
    if (expModal) {
        const modalForm = expModal.querySelector('#editExperienceForm');
        const editButtons = document.querySelectorAll('.btn-edit-experience');
        const closeButton = expModal.querySelector('.close-modal-btn');
        const overlay = expModal.closest('.modal-overlay');

        editButtons.forEach(button => {
            button.addEventListener('click', () => {
                const entryDiv = button.closest('.form-entry');
                const entryId = entryDiv.dataset.entryId;
                modalForm.action = `/update-experience/${entryId}/`;
                expModal.querySelector('#id_job_title').value = entryDiv.dataset.jobTitle;
                expModal.querySelector('#id_company').value = entryDiv.dataset.company;
                expModal.querySelector('#id_start_date').value = entryDiv.dataset.startDate;
                expModal.querySelector('#id_end_date').value = entryDiv.dataset.endDate;
                expModal.querySelector('#id_responsibilities').value = entryDiv.dataset.responsibilities;
                expModal.querySelector('#id_currently_work_here').checked = (entryDiv.dataset.currentlyWorkHere === 'true');
                expModal.querySelector('#id_is_internship').checked = (entryDiv.dataset.isInternship === 'true');
                overlay.style.display = 'flex';
            });
        });
        const closeExpModal = () => { overlay.style.display = 'none'; };
        closeButton.addEventListener('click', closeExpModal);
        overlay.addEventListener('click', e => { if (e.target === overlay) closeExpModal(); });
    }

    // --- SKILLS MODAL LOGIC ---
    const skillModal = document.getElementById('editSkillModal');
    if (skillModal) {
        const modalForm = skillModal.querySelector('#editSkillForm');
        const editButtons = document.querySelectorAll('.btn-edit-skill');
        const closeButton = skillModal.querySelector('.close-modal-btn');
        const overlay = skillModal.closest('.modal-overlay');

        editButtons.forEach(button => {
            button.addEventListener('click', () => {
                const entryDiv = button.closest('.form-entry');
                const entryId = entryDiv.dataset.entryId;
                modalForm.action = `/update-skill/${entryId}/`;
                skillModal.querySelector('#id_category').value = entryDiv.dataset.category;
                skillModal.querySelector('#id_skills_list').value = entryDiv.dataset.skillsList;
                overlay.style.display = 'flex';
            });
        });
        const closeSkillModal = () => { overlay.style.display = 'none'; };
        closeButton.addEventListener('click', closeSkillModal);
        overlay.addEventListener('click', e => { if (e.target === overlay) closeSkillModal(); });
    }

    // --- PROJECTS MODAL LOGIC ---
    const projectModal = document.getElementById('editProjectModal');
    if (projectModal) {
        const modalForm = projectModal.querySelector('#editProjectForm');
        const editButtons = document.querySelectorAll('.btn-edit-project');
        const closeButton = projectModal.querySelector('.close-modal-btn');
        const overlay = projectModal.closest('.modal-overlay');

        editButtons.forEach(button => {
            button.addEventListener('click', () => {
                const entryDiv = button.closest('.form-entry');
                const entryId = entryDiv.dataset.entryId;
                modalForm.action = `/update-project/${entryId}/`;
                projectModal.querySelector('#id_project_name').value = entryDiv.dataset.projectName;
                projectModal.querySelector('#id_project_link').value = entryDiv.dataset.projectLink;
                projectModal.querySelector('#id_description').value = entryDiv.dataset.description;
                overlay.style.display = 'flex';
            });
        });
        const closeProjectModal = () => { overlay.style.display = 'none'; };
        closeButton.addEventListener('click', closeProjectModal);
        overlay.addEventListener('click', e => { if (e.target === overlay) closeProjectModal(); });
    }
    
    // --- CERTIFICATIONS MODAL LOGIC ---
    const certModal = document.getElementById('editCertificationModal');
    if (certModal) {
        const modalForm = certModal.querySelector('#editCertificationForm');
        const editButtons = document.querySelectorAll('.btn-edit-certification');
        const closeButton = certModal.querySelector('.close-modal-btn');
        const overlay = certModal.closest('.modal-overlay');

        editButtons.forEach(button => {
            button.addEventListener('click', () => {
                const entryDiv = button.closest('.form-entry');
                const entryId = entryDiv.dataset.entryId;
                modalForm.action = `/update-certification/${entryId}/`;
                certModal.querySelector('#id_name').value = entryDiv.dataset.name;
                certModal.querySelector('#id_issuing_organization').value = entryDiv.dataset.issuingOrganization;
                certModal.querySelector('#id_date_issued').value = entryDiv.dataset.dateIssued;
                certModal.querySelector('#id_credential_url').value = entryDiv.dataset.credentialUrl;
                overlay.style.display = 'flex';
            });
        });
        const closeCertModal = () => { overlay.style.display = 'none'; };
        closeButton.addEventListener('click', closeCertModal);
        overlay.addEventListener('click', e => { if (e.target === overlay) closeCertModal(); });
    }

    // --- ACHIEVEMENTS MODAL LOGIC ---
    const achModal = document.getElementById('editAchievementModal');
    if (achModal) {
        const modalForm = achModal.querySelector('#editAchievementForm');
        const editButtons = document.querySelectorAll('.btn-edit-achievement');
        const closeButton = achModal.querySelector('.close-modal-btn');
        const overlay = achModal.closest('.modal-overlay');

        editButtons.forEach(button => {
            button.addEventListener('click', () => {
                const entryDiv = button.closest('.form-entry');
                const entryId = entryDiv.dataset.entryId;
                modalForm.action = `/update-achievement/${entryId}/`;
                achModal.querySelector('#id_description').value = entryDiv.dataset.description;
                overlay.style.display = 'flex';
            });
        });
        const closeAchModal = () => { overlay.style.display = 'none'; };
        closeButton.addEventListener('click', closeAchModal);
        overlay.addEventListener('click', e => { if (e.target === overlay) closeAchModal(); });
    }
});