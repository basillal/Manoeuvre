
/**
* Template Name: NiceAdmin - v2.5.0
* Template URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach(e => e.addEventListener(type, listener))
    } else {
      select(el, all).addEventListener(type, listener)
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Sidebar toggle
   */
  if (select('.toggle-sidebar-btn')) {
    on('click', '.toggle-sidebar-btn', function(e) {
      select('body').classList.toggle('toggle-sidebar')
    })
  }

  /**
   * Search bar toggle
   */
  if (select('.search-bar-toggle')) {
    on('click', '.search-bar-toggle', function(e) {
      select('.search-bar').classList.toggle('search-bar-show')
    })
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Initiate tooltips
   */
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })

  /**
   * Initiate quill editors
   */
  if (select('.quill-editor-default')) {
    new Quill('.quill-editor-default', {
      theme: 'snow'
    });
  }

  if (select('.quill-editor-bubble')) {
    new Quill('.quill-editor-bubble', {
      theme: 'bubble'
    });
  }

  if (select('.quill-editor-full')) {
    new Quill(".quill-editor-full", {
      modules: {
        toolbar: [
          [{
            font: []
          }, {
            size: []
          }],
          ["bold", "italic", "underline", "strike"],
          [{
              color: []
            },
            {
              background: []
            }
          ],
          [{
              script: "super"
            },
            {
              script: "sub"
            }
          ],
          [{
              list: "ordered"
            },
            {
              list: "bullet"
            },
            {
              indent: "-1"
            },
            {
              indent: "+1"
            }
          ],
          ["direction", {
            align: []
          }],
          ["link", "image", "video"],
          ["clean"]
        ]
      },
      theme: "snow"
    });
  }

  /**
   * Initiate TinyMCE Editor
   */
  const useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const isSmallScreen = window.matchMedia('(max-width: 1023.5px)').matches;

  tinymce.init({
    selector: 'textarea.tinymce-editor',
    plugins: 'preview importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons',
    editimage_cors_hosts: ['picsum.photos'],
    menubar: 'file edit view insert format tools table help',
    toolbar: 'undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl',
    toolbar_sticky: true,
    toolbar_sticky_offset: isSmallScreen ? 102 : 108,
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false,
    autosave_retention: '2m',
    image_advtab: true,
    link_list: [{
        title: 'My page 1',
        value: 'https://www.tiny.cloud'
      },
      {
        title: 'My page 2',
        value: 'http://www.moxiecode.com'
      }
    ],
    image_list: [{
        title: 'My page 1',
        value: 'https://www.tiny.cloud'
      },
      {
        title: 'My page 2',
        value: 'http://www.moxiecode.com'
      }
    ],
    image_class_list: [{
        title: 'None',
        value: ''
      },
      {
        title: 'Some class',
        value: 'class-name'
      }
    ],
    importcss_append: true,
    file_picker_callback: (callback, value, meta) => {
      /* Provide file and text for the link dialog */
      if (meta.filetype === 'file') {
        callback('https://www.google.com/logos/google.jpg', {
          text: 'My text'
        });
      }

      /* Provide image and alt text for the image dialog */
      if (meta.filetype === 'image') {
        callback('https://www.google.com/logos/google.jpg', {
          alt: 'My alt text'
        });
      }

      /* Provide alternative source and posted for the media dialog */
      if (meta.filetype === 'media') {
        callback('movie.mp4', {
          source2: 'alt.ogg',
          poster: 'https://www.google.com/logos/google.jpg'
        });
      }
    },
    templates: [{
        title: 'New Table',
        description: 'creates a new table',
        content: '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>'
      },
      {
        title: 'Starting my story',
        description: 'A cure for writers block',
        content: 'Once upon a time...'
      },
      {
        title: 'New list with dates',
        description: 'New List with dates',
        content: '<div class="mceTmpl"><span class="cdate">cdate</span><br><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>'
      }
    ],
    template_cdate_format: '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
    template_mdate_format: '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
    height: 600,
    image_caption: true,
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
    noneditable_class: 'mceNonEditable',
    toolbar_mode: 'sliding',
    contextmenu: 'link image table',
    skin: useDarkMode ? 'oxide-dark' : 'oxide',
    content_css: useDarkMode ? 'dark' : 'default',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }'
  });

  /**
   * Initiate Bootstrap validation check
   */
  var needsValidation = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(needsValidation)
    .forEach(function(form) {
      form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })

  /**
   * Initiate Datatables
   */
  const datatables = select('.datatable', true)
  datatables.forEach(datatable => {
    new simpleDatatables.DataTable(datatable);
  })

  /**
   * Autoresize echart charts
   */
  const mainContainer = select('#main');
  if (mainContainer) {
    setTimeout(() => {
      new ResizeObserver(function() {
        select('.echart', true).forEach(getEchart => {
          echarts.getInstanceByDom(getEchart).resize();
        })
      }).observe(mainContainer);
    }, 200);
  }

})();


// ************** REGISTRATION MODAL *******************

let setCount, idCount, groupno, isGroup = false;

$(document).ready(function() {

  // ********* Add a click event handler to the registrationBtn link ******
  $(".ITMregistrationBtn").click(function() {
    // Show the registrationModal when the link is clicked
    //$("#registrationModal").modal('show');
    window.location.href = 'itmanager/';
  });
  $(".webregistrationBtn").click(function() {
    // Show the registrationModal when the link is clicked
    //$("#registrationModal").modal('show');
    window.location.href = 'webdesigning/';
  });
  
  $(".closeModal").click(function() {
    // Close the registrationModal when clicked
    $("#registrationModal").modal('hide')
  });
  
  
  // ******** Adding participant *******



  // ******************  Function to Add New Participant  *********************************************************
  function addItem(count){
    count++; // change index 0 to 1
    idCount++; // Change id count by 1

    // Cloning first participant detail container
    var newParticipant = $(".participant-details-template:first").clone();

    // Clear the values in the cloned fields
    newParticipant.find('.participant-name').attr('id', 'participant' + (idCount)).attr('name', 'participant' + (count)).attr('placeholder', 'Participant ' + (count) + ' Name');
    newParticipant.find('.register-number').attr('id', 'registerno' + (idCount)).attr('name', 'register_no' + (count));

    // Change the display hidden to default
    newParticipant.css('display', '');

    // Append the cloned section to the form
    newParticipant.appendTo('.participant-details');
  }
 


  $(".add-participant").click((e)=>{
    e.preventDefault();
    if(isGroup){
      groupno++;
      $('.isgroup').css('display', 'block');
      $('.isgroup').text("Group 1");

      //For making a heading like Group 1, Group 2
      var newHeading = $("<h5></h5>");

      // Set content for the new element
      newHeading.text("Group "+groupno);

      // Append the new element to an existing element
      newHeading.appendTo(".participant-details");

      // Grouping divs
      for (let index = 0; index < minCountValue; index++) {
        addItem(index);  
      }
      
    }
    else{
      addItem(setCount++);
    }
  });


  // *************** For default selected item ***************
  let selectedOption = $("#event-name").find("option:selected").val();
  let minCountValue = $("#event-name").find("option:selected").attr("mincount");

  // Setting to continue with the numbering when adding new participant
  setCount = parseInt(minCountValue);
  idCount = 0;
  for (let index = 0; index < minCountValue; index++) {
    addItem(index);      
  }


  // ***************** Change in select box *****************

  $("#event-name").change(function() {
    selectedOption = $(this).find("option:selected");

    // Get the value of the "mincount" attribute
    minCountValue = parseInt(selectedOption.attr("mincount"));

    // Setting the mincount as setCount again
    setCount = minCountValue;

    groupno = 1;
    idCount = 0;

    isGroup = ($(selectedOption).attr("group") !== undefined) ? true : false;

    if(isGroup){
      $('.isgroup').css('display', 'block');
      $('.isgroup').text("Group 1");
    }
    else{
      $('.isgroup').css('display', 'none');
    }

    // Clearing existing participant details
    $(".participant-details").empty();
    

    // Clone and append the participant details template based on "mincount"
    for (let index = 0; index < minCountValue; index++) {
      addItem(index);      
    }
    
  });

  // $(".register-event").click((e)=> {
  //   e.preventDefault();
  //   console.log("registered");
    
    
  //   // })
  // });

  // Function to perform registration
  $('#registrationForm').submit(function (e) {
    e.preventDefault(); // Prevent default form submission

    var formData = $(this).serialize(); // Serialize the form data

    $.ajax({
        url: '/event_registration/', // Replace with your URL
        type: 'POST',
        data: formData, // Include serialized form data
        success: function (response) {
            console.log(response);
            callToast(); // Handle the response from the server
            $('#registrationForm')[0].reset();
        },
        error: function () {
            console.log('Error submitting form');
        }
    });
});



});


// ************* END OF REGISTRATION FORM ***********************

// TOAST MESSAGE 
function callToast() {
  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(()=> { 
    x.className = x.className.replace("show", "");
  }, 3000);
}