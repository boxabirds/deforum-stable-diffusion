# Template to take colab parameters scoped inside methods (e.g. Root, DeforumArgs, etc.) 
# and generate a parameters.py file with python type hinting
# that can be used by libraries and APIs for validation of input
# the intention is that this file be autogenerated from a source ipynb file.
# This file was automatically generated. Do not edit -- rather rerun the file "extract_colab_parameters.py"
# jinja2 template: parameters.tmpl.py
# example input file: parameters.json

class DeforumAnimArgs:
      animation_mode: str = "'None'"  # None, 2D, 3D, Video Input, Interpolation
      max_frames: float = 1000
      border: str = "'replicate'"  # wrap, replicate
      angle: str = "0:(0)"
      zoom: str = "0:(1.04)"
      translation_x: str = "0:(10*sin(2*3.14*t/10))"
      translation_y: str = "0:(0)"
      translation_z: str = "0:(10)"
      rotation_3d_x: str = "0:(0)"
      rotation_3d_y: str = "0:(0)"
      rotation_3d_z: str = "0:(0)"
      flip_2d_perspective: bool = False
      perspective_flip_theta: str = "0:(0)"
      perspective_flip_phi: str = "0:(t%15)"
      perspective_flip_gamma: str = "0:(0)"
      perspective_flip_fv: str = "0:(53)"
      noise_schedule: str = "0: (0.02)"
      strength_schedule: str = "0: (0.65)"
      contrast_schedule: str = "0: (1.0)"
      hybrid_video_comp_alpha_schedule: str = "0:(1)"
      hybrid_video_comp_mask_blend_alpha_schedule: str = "0:(0.5)"
      hybrid_video_comp_mask_contrast_schedule: str = "0:(1)"
      hybrid_video_comp_mask_auto_contrast_cutoff_high_schedule: str = "0:(100)"
      hybrid_video_comp_mask_auto_contrast_cutoff_low_schedule: str = "0:(0)"
      kernel_schedule: str = "0: (5)"
      sigma_schedule: str = "0: (1.0)"
      amount_schedule: str = "0: (0.2)"
      threshold_schedule: str = "0: (0.0)"
      color_coherence: str = "'Match Frame 0 LAB'"  # None, Match Frame 0 HSV, Match Frame 0 LAB, Match Frame 0 RGB, Video Input
      color_coherence_video_every_N_frames: int = 1
      diffusion_cadence: str = "'1'"  # 1, 2, 3, 4, 5, 6, 7, 8
      use_depth_warping: bool = True
      midas_weight: float = 0.3
      fov: float = 40
      padding_mode: str = "'border'"  # border, reflection, zeros
      sampling_mode: str = "'bicubic'"  # bicubic, bilinear, nearest
      save_depth_maps: bool = False
      video_init_path: str = "'/content/video_in.mp4'"
      extract_nth_frame: float = 1
      overwrite_extracted_frames: bool = True
      use_mask_video: bool = False
      video_mask_path: str = "'/content/video_in.mp4'"
      hybrid_video_generate_inputframes: bool = False
      hybrid_video_use_first_frame_as_init_image: bool = True
      hybrid_video_motion = "None"  # None, Optical Flow, Perspective, Affine
      hybrid_video_flow_method = "Farneback"  # Farneback, DenseRLOF, SF
      hybrid_video_composite: bool = False
      hybrid_video_comp_mask_type = "None"  # None, Depth, Video Depth, Blend, Difference
      hybrid_video_comp_mask_inverse: bool = False
      hybrid_video_comp_mask_equalize = "None"  # None, Before, After, Both
      hybrid_video_comp_mask_auto_contrast: bool = False
      hybrid_video_comp_save_extra_frames: bool = False
      hybrid_video_use_video_as_mse_image: bool = False
      interpolate_key_frames: bool = False
      interpolate_x_frames: float = 4
      resume_from_timestring: bool = False
      resume_timestring: str = "20220829210106"
class Root:
      models_path: str = "models"
      configs_path: str = "configs"
      output_path: str = "outputs"
      mount_google_drive: bool = True
      models_path_gdrive: str = "/content/drive/MyDrive/AI/models"
      output_path_gdrive: str = "/content/drive/MyDrive/AI/StableDiffusion"
      map_location = "cuda"  # cpu, cuda
      model_config = "v1-inference.yaml"  # custom, v2-inference.yaml, v2-inference-v.yaml, v1-inference.yaml
      model_checkpoint = "Protogen_V2.2.ckpt"  # custom, v2-1_768-ema-pruned.ckpt, v2-1_512-ema-pruned.ckpt, 768-v-ema.ckpt, 512-base-ema.ckpt, Protogen_V2.2.ckpt, v1-5-pruned.ckpt, v1-5-pruned-emaonly.ckpt, sd-v1-4-full-ema.ckpt, sd-v1-4.ckpt, sd-v1-3-full-ema.ckpt, sd-v1-3.ckpt, sd-v1-2-full-ema.ckpt, sd-v1-2.ckpt, sd-v1-1-full-ema.ckpt, sd-v1-1.ckpt, robo-diffusion-v1.ckpt, wd-v1-3-float16.ckpt
      custom_config_path: str = ""
      custom_checkpoint_path: str = ""
class DeforumArgs:
      override_settings_with_file: bool = False
      settings_file = "custom"  # custom, 512x512_aesthetic_0.json, 512x512_aesthetic_1.json, 512x512_colormatch_0.json, 512x512_colormatch_1.json, 512x512_colormatch_2.json, 512x512_colormatch_3.json
      custom_settings_file: str = "/content/drive/MyDrive/Settings.txt"
      W = "512"
      H = "512"
      bit_depth_output: str = "8"  # 8, 16, 32
      seed = "-1"
      sampler = "'euler_ancestral'"  # klms, dpm2, dpm2_ancestral, heun, euler, euler_ancestral, plms, ddim, dpm_fast, dpm_adaptive, dpmpp_2s_a, dpmpp_2m
      steps = "50"
      scale = "7"
      ddim_eta = "0.0"
      save_samples: bool = True
      save_settings: bool = True
      display_samples: bool = True
      save_sample_per_step: bool = False
      show_sample_per_step: bool = False
      prompt_weighting: bool = True
      normalize_prompt_weights: bool = True
      log_weighted_subprompts: bool = False
      n_batch = "1"
      batch_name: str = "StableFun"
      filename_format = "{timestring}_{index}_{prompt}.png"  # {timestring}_{index}_{seed}.png, {timestring}_{index}_{prompt}.png
      seed_behavior = "iter"  # iter, fixed, random, ladder, alternate
      seed_iter_N: int = 1
      make_grid: bool = False
      grid_rows = "2"
      use_init: bool = False
      strength: float = 0.1
      init_image: str = "https://cdn.pixabay.com/photo/2022/07/30/13/10/green-longhorn-beetle-7353749_1280.jpg"
      use_mask: bool = False
      mask_file: str = "https://www.filterforge.com/wiki/images/archive/b/b7/20080927223728%21Polygonal_gradient_thumb.jpg"
      invert_mask: bool = False
      mask_brightness_adjust: float = 1.0
      mask_contrast_adjust: float = 1.0
      mean_scale: float = 0
      var_scale: float = 0
      exposure_scale: float = 0
      exposure_target: float = 0.5
      colormatch_scale: float = 0
      colormatch_image: str = "https://www.saasdesign.io/wp-content/uploads/2021/02/palette-3-min-980x588.png"
      colormatch_n_colors: float = 4
      ignore_sat_weight: float = 0
      clip_name = "'ViT-L/14'"  # ViT-L/14, ViT-L/14@336px, ViT-B/16, ViT-B/32
      clip_scale: float = 0
      aesthetics_scale: float = 0
      cutn: float = 1
      cut_pow: float = 0.0001
      init_mse_scale: float = 0
      init_mse_image: str = "https://cdn.pixabay.com/photo/2022/07/30/13/10/green-longhorn-beetle-7353749_1280.jpg"
      blue_scale: float = 0
      gradient_wrt = "'x0_pred'"  # x, x0_pred
      gradient_add_to = "'both'"  # cond, uncond, both
      decode_method = "'linear'"  # autoencoder, linear
      grad_threshold_type = "'dynamic'"  # dynamic, static, mean, schedule
      clamp_grad_threshold: float = 0.2
      clamp_start = "0.2"
      clamp_stop = "0.01"
      grad_inject_timing = "list(range(1,10))"
      cond_uncond_sync: bool = True
class BasicArgs:
      skip_video_for_run_all: bool = True
      fps: float = 12
      use_manual_settings: bool = False
      image_path: str = "/content/drive/MyDrive/AI/StableDiffusion/2023-01/StableFun/20230101212135_%05d.png"
      mp4_path: str = "/content/drive/MyDrive/AI/StableDiffusion/2023-01/StableFun/20230101212135.mp4"
      render_steps: bool = False
      path_name_modifier = "x0_pred"  # x0_pred, x
      skip_disconnect_for_run_all: bool = True
      max_frames: str = "200"
