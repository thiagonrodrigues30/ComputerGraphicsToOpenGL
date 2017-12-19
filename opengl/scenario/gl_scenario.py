import copy
import os
from OpenGL.GL import *

from ray_casting.objectModeling import obj
from ray_casting.transformations import model_transformations as mt

def draw_scenario_corrida():


    ########### Definindo Cenario ###########
    # importando os objetos ja setados, talvez precise modificar depois
    path = os.path.normpath(os.path.join(__file__, '../../../objects/cube2.obj'))
    cube = obj.Obj().import_obj(path)

    # MATERIAIS
    # Cores dos Materiais & Componentes Especulares:
    specular_term = [1, 1, 1]
    specular_term2 = [0.3, 0.3, 0.3]
    rugose_term = [0.2, 0.2, 0.2]
    m = 10

    # MATERIAL ASFALTO
    rgb_asfalto_material = [0.50196078, 0.50196078, 0.50196078]
    asfalto_material = obj.Material(rgb_asfalto_material, rgb_asfalto_material, specular_term2, m)
    asfalto_cube = copy.deepcopy(cube)
    asfalto_cube.apply_material(asfalto_material)

    # MATERIAL GRAMADO
    rgb_gramado_material = [50 / 255, 205 / 255, 50 / 255]
    gramado_material = obj.Material(rgb_gramado_material, rgb_gramado_material, specular_term, m)
    gramado_cube = copy.deepcopy(cube)
    gramado_cube.apply_material(gramado_material)

    # MATERIAL MADEIRA
    rgb_madeira_material = [92 / 255, 51 / 255, 23 / 255]
    madeira_material = obj.Material(rgb_madeira_material, rgb_madeira_material, specular_term, 2)
    madeira_cube = copy.deepcopy(cube)
    madeira_cube.apply_material(gramado_material)

    # MATERIAL LINHA DE CHEGADA 1
    rgb_chegada1_material = [0, 0, 0]
    chegada1_material = obj.Material(rgb_chegada1_material, rgb_chegada1_material, specular_term, m)
    chegada1_cube = copy.deepcopy(cube)
    chegada1_cube.apply_material(chegada1_material)

    # MATERIAL LINHA DE CHEGADA 2
    rgb_chegada2_material = [1, 1, 1]
    chegada2_material = obj.Material(rgb_chegada2_material, rgb_chegada2_material, specular_term, m)
    chegada2_cube = copy.deepcopy(cube)
    chegada2_cube.apply_material(chegada2_material)

    # MATERIAL POSTE 1
    rgb_poste1_material = [140 / 255, 23 / 255, 23 / 255]
    poste1_material = obj.Material(rgb_poste1_material, rgb_poste1_material, specular_term, 2)
    poste1_cube = copy.deepcopy(cube)
    poste1_cube.apply_material(poste1_material)

    # MATERIAL POSTE 2
    rgb_poste2_material = [207 / 255, 181 / 255, 59 / 255]
    poste2_material = obj.Material(rgb_poste2_material, rgb_poste2_material, specular_term, 2)
    poste2_cube = copy.deepcopy(cube)
    poste2_cube.apply_material(poste2_material)


    ####################


    # GRAMADO
    glPushMatrix()
    #glScalef(3., 0.1, 4.)
    glScalef(150, 0.01, 150)
    draw_polygon(gramado_cube)
    glPopMatrix()



def draw_scenario():
    path = os.path.normpath(os.path.join(__file__,'../../../objects/cube2.obj'))
    cube = obj.Obj().import_obj(path)

    # MATERIALS

    specular_term = [0.3, 0.3, 0.3]
    m = 0.1
    # WALLS MATERIAL
    rgb_wall_material = [44 / 255, 137 / 255, 142 / 255]
    wall_material = obj.Material(rgb_wall_material, rgb_wall_material, specular_term, m)
    wall_cube = copy.deepcopy(cube)
    wall_cube.apply_material(wall_material)

    # CEILING MATERIAL
    rgb_ceiling_material = [200 / 255, 203 / 255, 208 / 255]
    ceiling_material = obj.Material(rgb_ceiling_material, rgb_ceiling_material, specular_term, m)
    ceiling_cube = copy.deepcopy(cube)
    ceiling_cube.apply_material(ceiling_material)

    # FLOOR MATERIAL
    floor_material = obj.Material(rgb_ceiling_material, rgb_ceiling_material, specular_term, m)
    floor_cube = copy.deepcopy(cube)
    floor_cube.apply_material(floor_material)

    #  BLACK MATERIAL
    rgb_black = [0, 0, 0]
    black_material = obj.Material(rgb_black, rgb_black, specular_term, 5)
    black_cube = copy.deepcopy(cube)
    black_cube.apply_material(black_material)

    # WOOD MATERIAL
    rgb_wood_dark = [89 / 255, 63 / 255, 44 / 255]
    rgb_wood_light = [144 / 255, 112 / 255, 100 / 255]
    wood_material_dark = obj.Material(rgb_wood_dark, rgb_wood_dark, specular_term, m)
    wood_material_light = obj.Material(rgb_wood_light, rgb_wood_light, specular_term, m)
    dark_wood_cube = copy.deepcopy(cube)
    dark_wood_cube.apply_material(wood_material_dark)
    light_wood_cube = copy.deepcopy(cube)
    light_wood_cube.apply_material(wood_material_light)

    # SOFA MATERIAL
    rgb_sofa = [93 / 255, 83 / 255, 87 / 255]
    sofa_material = obj.Material(rgb_sofa, rgb_sofa, specular_term, m)
    sofa_cube = copy.deepcopy(cube)
    sofa_cube.apply_material(sofa_material)

    rgb_gray_light = [144 / 255, 150 / 255, 169 / 255]
    gray_material_light = obj.Material(rgb_gray_light, rgb_gray_light, specular_term, m)
    gray_cube = copy.deepcopy(cube)
    gray_cube.apply_material(gray_material_light)

    # CHÃO
    glPushMatrix()
    glScalef(3., 0.1, 4.)
    draw_polygon(floor_cube)
    glPopMatrix()

    # TETO
    glPushMatrix()
    glTranslatef(0, 3., 0)
    glScalef(3., 0.1, 4.)
    draw_polygon(ceiling_cube)
    glPopMatrix()

    # TETO: DETALHES - TRÁS
    glPushMatrix()
    glTranslatef(0.1, 2.7, 0.1)
    glScalef(2.8, 0.3, 0.8)
    draw_polygon(ceiling_cube)
    glPopMatrix()

    # TETO: DETALHES - FRENTE
    glPushMatrix()
    glTranslatef(0.1, 2.7, 3.1)
    glScalef(2.8, 0.3, 0.8)
    draw_polygon(ceiling_cube)
    glPopMatrix()

    # TETO: DETALHES - ESQUERDA
    glPushMatrix()
    glTranslatef(0.1, 2.7, 0.9)
    glScalef(0.5, 0.3, 2.3)
    draw_polygon(ceiling_cube)
    glPopMatrix()

    # TETO: DETALHES - DIREITA
    glPushMatrix()
    glTranslatef(2.4, 2.7, 0.9)
    glScalef(0.5, 0.3, 2.3)
    draw_polygon(ceiling_cube)
    glPopMatrix()

    # PAREDE TRÁS
    glPushMatrix()
    glScalef(3., 3., 0.1)
    draw_polygon(wall_cube)
    glPopMatrix()

    # PAREDE TRÁS: DETALHES - ESQUERDA
    glPushMatrix()
    glTranslatef(0.1, 0.1, 0.1)
    glScalef(0.4, 2.6, 0.3)
    draw_polygon(dark_wood_cube)
    glPopMatrix()

    # PAREDE TRÁS: DETALHES - DIREITA
    glPushMatrix()
    glTranslatef(2.5, 0.1, 0.1)
    glScalef(0.4, 2.6, 0.3)
    draw_polygon(dark_wood_cube)
    glPopMatrix()

    # PAREDE TRÁS: DETALHES - ESQUERDA-CIMA
    glPushMatrix()
    glTranslatef(0.5, 1.7, 0.1)
    glScalef(0.5, 1.0, 0.3)
    draw_polygon(dark_wood_cube)
    glPopMatrix()

    # PAREDE TRÁS: DETALHES - DIREITA-CIMA
    glPushMatrix()
    glTranslatef(2.0, 1.7, 0.1)
    glScalef(0.5, 1.0, 0.3)
    draw_polygon(dark_wood_cube)
    glPopMatrix()

    # PRATELEIRAS DA PAREDE DE TRÁS - BAIXO
    glPushMatrix()
    glTranslatef(1.0, 1.9, 0.1)
    glScalef(1.0, 0.06, 0.25)
    draw_polygon(dark_wood_cube)
    glPopMatrix()

    # PRATELEIRAS DA PAREDE DE TRÁS - MEIO
    glPushMatrix()
    glTranslatef(1.0, 2.2, 0.1)
    glScalef(1.0, 0.06, 0.25)
    draw_polygon(dark_wood_cube)
    glPopMatrix()

    # PRATELEIRAS DA PAREDE DE TRÁS - CIMA
    glPushMatrix()
    glTranslatef(1.0, 2.5, 0.1)
    glScalef(1.0, 0.06, 0.25)
    draw_polygon(dark_wood_cube)
    glPopMatrix()

    # TV - CENTRO
    glPushMatrix()
    glTranslatef(1.0, 0.8, 0.1)
    glScalef(1.0, 0.6, 0.05)
    draw_polygon(gray_cube)
    glPopMatrix()

    # TV - BORDA ESQUERDA
    glPushMatrix()
    glTranslatef(0.94, 0.8, 0.1)
    glScalef(0.06, 0.6, 0.08)
    draw_polygon(black_cube)
    glPopMatrix()

    # TV - BORDA DIREITA
    glPushMatrix()
    glTranslatef(2.0, 0.8, 0.1)
    glScalef(0.06, 0.6, 0.08)
    draw_polygon(black_cube)
    glPopMatrix()

    # TV - BORDA BAIXO
    glPushMatrix()
    glTranslatef(0.94, 0.74, 0.1)
    glScalef(1.12, 0.06, 0.08)
    draw_polygon(black_cube)
    glPopMatrix()

    # TV - BORDA CIMA
    glPushMatrix()
    glTranslatef(0.94, 1.4, 0.1)
    glScalef(1.12, 0.06, 0.08)
    draw_polygon(black_cube)
    glPopMatrix()

    # TV RACK - BAIXO
    glPushMatrix()
    glTranslatef(0.9, 0.2, 0.1)
    glScalef(1.2, 0.06, 0.4)
    draw_polygon(light_wood_cube)
    glPopMatrix()

    # TV RACK - CIMA
    glPushMatrix()
    glTranslatef(0.9, 0.4, 0.1)
    glScalef(1.2, 0.06, 0.4)
    draw_polygon(light_wood_cube)
    glPopMatrix()

    # TV RACK - ESQUERDA
    glPushMatrix()
    glTranslatef(0.95, 0, 0.1)
    glScalef(0.06, 0.4, 0.35)
    draw_polygon(light_wood_cube)
    glPopMatrix()

    # TV RACK - DIREITA
    glPushMatrix()
    glTranslatef(1.99, 0, 0.1)
    glScalef(0.06, 0.4, 0.35)
    draw_polygon(light_wood_cube)
    glPopMatrix()

    # SPEAKER - ESQUERDA
    glPushMatrix()
    glTranslatef(0.6, 0, 0.1)
    glScalef(0.2, 0.9, 0.3)
    draw_polygon(black_cube)
    glPopMatrix()

    # SPEAKER - DIREITA
    glPushMatrix()
    glTranslatef(2.2, 0, 0.1)
    glScalef(0.2, 0.9, 0.3)
    draw_polygon(black_cube)
    glPopMatrix()

    # SPEAKER - APARELHO
    glPushMatrix()
    glTranslatef(1.2, 0.46, 0.1)
    glScalef(0.6, 0.2, 0.3)
    draw_polygon(black_cube)
    glPopMatrix()

    # SOFA 1 - COSTAS
    glPushMatrix()
    glTranslatef(0.15, 0.1, 1.25)
    glScalef(0.15, 0.8, 1.5)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 1 - BRAÇO DIREITA
    glPushMatrix()
    glTranslatef(0.3, 0.1, 1.25)
    glScalef(0.6, 0.6, 0.15)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 1 - BRAÇO ESQUERDA
    glPushMatrix()
    glTranslatef(0.3, 0.1, 2.6)
    glScalef(0.6, 0.6, 0.15)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 1 - BASE
    glPushMatrix()
    glTranslatef(0.3, 0.05, 1.4)
    glScalef(0.6, 0.3, 1.2)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 1 - ASSENTO 1
    glPushMatrix()
    glTranslatef(0.3, 0.35, 1.38)
    glScalef(0.6, 0.05, 0.61)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 1 - ASSENTO 2
    glPushMatrix()
    glTranslatef(0.3, 0.35, 2.0)
    glScalef(0.6, 0.05, 0.61)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 2 - COSTAS
    glPushMatrix()
    glTranslatef(2.7, 0.1, 1.25)
    glScalef(0.15, 0.8, 1.5)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 2 - BRAÇO DIREITA
    glPushMatrix()
    glTranslatef(2.1, 0.1, 1.25)
    glScalef(0.6, 0.6, 0.15)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 2 - BRAÇO ESQUERDA
    glPushMatrix()
    glTranslatef(2.1, 0.1, 2.6)
    glScalef(0.6, 0.6, 0.15)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 2 - BASE
    glPushMatrix()
    glTranslatef(2.1, 0.05, 1.4)
    glScalef(0.6, 0.3, 1.2)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 2 - ASSENTO 1
    glPushMatrix()
    glTranslatef(2.1, 0.35, 1.38)
    glScalef(0.6, 0.05, 0.61)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # SOFA 2 - ASSENTO 2
    glPushMatrix()
    glTranslatef(2.1, 0.35, 2.0)
    glScalef(0.6, 0.05, 0.61)
    draw_polygon(sofa_cube)
    glPopMatrix()

    # MESA - CIMA
    glPushMatrix()
    glTranslatef(1.2, 0.3, 1.5)
    glScalef(0.6, 0.1, 1.0)
    draw_polygon(light_wood_cube)
    glPopMatrix()

    # MESA - APOIO TRÁS
    glPushMatrix()
    glTranslatef(1.25, 0.1, 1.6)
    glScalef(0.5, 0.2, 0.2)
    draw_polygon(light_wood_cube)
    glPopMatrix()

    # MESA - APOIO FRENTE
    glPushMatrix()
    glTranslatef(1.25, 0.1, 2.2)
    glScalef(0.5, 0.2, 0.2)
    draw_polygon(light_wood_cube)
    glPopMatrix()

    # PAREDE FRENTE
    glPushMatrix()
    glTranslatef(0, 0, 3.9)
    glScalef(3., 3., 0.1)
    draw_polygon(wall_cube)
    glPopMatrix()

    # PAREDE ESQUERDA - LATERAL
    glPushMatrix()
    glTranslatef(0, 1, 0)
    glScalef(0.1, 1.4, 0.75)
    draw_polygon(wall_cube)
    glPopMatrix()

    # PAREDE ESQUERDA - MEIO
    glPushMatrix()
    glTranslatef(0, 1, 1.75)
    glScalef(0.1, 1.4, 0.5)
    draw_polygon(wall_cube)
    glPopMatrix()

    # PAREDE ESQUERDA - LATERAL
    glPushMatrix()
    glTranslatef(0, 1, 3.25)
    glScalef(0.1, 1.4, 0.75)
    draw_polygon(wall_cube)
    glPopMatrix()

    # PAREDE ESQUERDA - BAIXO
    glPushMatrix()
    glScalef(0.1, 1., 4.)
    draw_polygon(wall_cube)
    glPopMatrix()

    # PAREDE ESQUERDA - CIMA
    glPushMatrix()
    glTranslatef(0, 2.4, 0)
    glScalef(0.1, 0.6, 4.)
    draw_polygon(wall_cube)
    glPopMatrix()

    # PERSIANAS
    sh = mt.get_shear_matrix('x', 'y', -45)
    for x in range(0, 17):
        glPushMatrix()
        glTranslatef(0.125, 1.05 + (x * 0.08), 0.75)
        glMultMatrixf(sh)
        glScalef(0.03, 0.01, 1.05)
        draw_polygon(cube)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.125, 1.05 + (x * 0.08), 2.2)
        glMultMatrixf(sh)
        glScalef(0.03, 0.01, 1.05)
        draw_polygon(cube)
        glPopMatrix()

    # PAREDE DIREITA
    glPushMatrix()
    glTranslatef(2.9, 0., 0.)
    glScalef(0.1, 3., 4.)
    draw_polygon(wall_cube)
    glPopMatrix()


def draw_polygon(obj):
    for face in obj.faces:
        glMaterialfv(GL_FRONT, GL_AMBIENT, face.material.k_a_rgb)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, face.material.k_d_rgb)
        glMaterialfv(GL_FRONT, GL_SPECULAR, face.material.k_e_rgb)
        glMaterialf(GL_FRONT, GL_SHININESS, face.material.attenuation)

        glBegin(GL_POLYGON)
        for vertex in face.vertices:
            glNormal3fv(vertex.normal)
            glVertex3fv(vertex.coordinates[:3])
        glEnd()
        '''
        glBegin(GL_LINES)
        for vertex in face.vertices:
            vx = vertex.coordinates[0] + vertex.normal[0]
            vy = vertex.coordinates[1] + vertex.normal[1]
            vz = vertex.coordinates[2] + vertex.normal[2]
            glVertex3f(vx, vy, vz)
            glVertex3fv(vertex.coordinates[:3])
        glEnd()
        '''
