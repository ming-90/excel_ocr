const change_image = async (e) => {
    file_name = e.target.files[0].name
    $("#input_text").val(file_name)
    file_type = e.target.files[0].type

    file = e.target.files[0]
    console.log(file)
    show_image(file)

    let formData = new FormData()
    formData.append("image", file, "image.jpg")
    await fetch("/infer", {
        method: 'POST',
        body: formData,
        headers:{
            accept: "application/json",
        }
    }).then((response) => response.json())
    .then((data) => {
        console.log(data)
        $.each(data, function(idx, val) {
            console.log(val)
            s = new dfd.Series(val)
            s.print()

        })
    })
}

const show_image = (file) => {
    type = file.type
    if(type.split("/")[0] == "image"){
        create_tag(".pdf-viewer", "image")
    }else if(type.split("/")[0] == "application/pdf"){
        create_tag(".pdf-viewer", "pdf")
    }
    url = window.URL.createObjectURL(file)
    $("#file").attr("src", url)
}

const create_tag = (parent, type) => {
    tag = ""
    if(type == "image"){
        tag = `
            <image class=image id=file></image>
        `
    }else{
        tag = `
            <iframe></iframe>
        `
    }
    $(parent).html(tag)
}